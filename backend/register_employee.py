import cv2
import uuid
import customtkinter as ctk
from tkinter import messagebox
from config import (
    s3,
    rekognition,
    employee_table,
    BUCKET_NAME,
    COLLECTION_ID
)

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Identiq - Register Employee")
app.geometry("500x500")
app.resizable(False, False)

title = ctk.CTkLabel(
    app,
    text="Register Employee",
    font=("Arial", 24, "bold")
)
title.pack(pady=20)

employee_id_entry = ctk.CTkEntry(
    app,
    width=300,
    placeholder_text="Employee ID"
)
employee_id_entry.pack(pady=10)

name_entry = ctk.CTkEntry(
    app,
    width=300,
    placeholder_text="Employee Name"
)
name_entry.pack(pady=10)

department_entry = ctk.CTkEntry(
    app,
    width=300,
    placeholder_text="Department"
)
department_entry.pack(pady=10)

email_entry = ctk.CTkEntry(
    app,
    width=300,
    placeholder_text="Email"
)
email_entry.pack(pady=10)


def register():
    employee_id = employee_id_entry.get().strip()
    name = name_entry.get().strip()
    department = department_entry.get().strip()
    email = email_entry.get().strip()

    if (
        employee_id == "" or
        name == "" or
        department == "" or
        email == ""
    ):
        messagebox.showerror(
            "Error",
            "Fill all fields."
        )
        return

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        cv2.imshow(
            "Press SPACE to Capture",
            frame
        )

        key = cv2.waitKey(1)
        if key == 32:  # SPACE

            filename = f"{uuid.uuid4()}.jpg"

            cv2.imwrite(
                filename,
                frame
            )

            cap.release()
            cv2.destroyAllWindows()

            # Upload image to S3
            s3.upload_file(
                filename,
                BUCKET_NAME,
                f"employees/{filename}"
            )

            # Index face into Rekognition Collection
            rekognition.index_faces(
                CollectionId=COLLECTION_ID,
                Image={
                    "S3Object": {
                        "Bucket": BUCKET_NAME,
                        "Name": f"employees/{filename}"
                    }
                },
                ExternalImageId=employee_id,
                DetectionAttributes=[]
            )

            # Save employee details in DynamoDB
            employee_table.put_item(
                Item={
                    "employee_id": employee_id,
                    "name": name,
                    "department": department,
                    "email": email
                }
            )

            messagebox.showinfo(
                "Success",
                "Employee Registered Successfully!"
            )

            break

        elif key == 27:  # ESC

            cap.release()
            cv2.destroyAllWindows()
            return

    cap.release()
    cv2.destroyAllWindows()


register_btn = ctk.CTkButton(
    app,
    text="📸 Register Employee",
    command=register,
    width=250,
    height=40,
    fg_color="green"
)

register_btn.pack(pady=30)

app.mainloop()