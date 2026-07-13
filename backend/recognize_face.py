import cv2
import uuid
import os
from datetime import datetime
from tkinter import messagebox

from config import (
    s3,
    rekognition,
    attendance_table,
    BUCKET_NAME,
    COLLECTION_ID
)


def recognize():

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        cv2.imshow(
            "Press SPACE to Capture Attendance",
            frame
        )

        key = cv2.waitKey(1)

        if key == 32:

            filename = f"{uuid.uuid4()}.jpg"

            cv2.imwrite(
                filename,
                frame
            )

            cap.release()
            cv2.destroyAllWindows()

            s3.upload_file(
                filename,
                BUCKET_NAME,
                f"attendance-images/{filename}"
            )

            response = rekognition.search_faces_by_image(
                CollectionId=COLLECTION_ID,
                Image={
                    "S3Object": {
                        "Bucket": BUCKET_NAME,
                        "Name": f"attendance-images/{filename}"
                    }
                },
                FaceMatchThreshold=90,
                MaxFaces=1
            )

            os.remove(filename)

            if len(response["FaceMatches"]) == 0:

                messagebox.showerror(
                    "Identiq",
                    "Employee not recognized."
                )

                return

            employee_id = response["FaceMatches"][0]["Face"]["ExternalImageId"]

            today = datetime.now().strftime("%Y-%m-%d")
            current_time = datetime.now().strftime("%H:%M:%S")

            response = attendance_table.scan()

            items = response.get("Items", [])

            today_record = None

            for item in items:

                if (
                    item["employee_id"] == employee_id
                    and item["date"] == today
                ):
                    today_record = item
                    break

            if today_record is None:

                attendance_table.put_item(
                    Item={
                        "employee_id": employee_id,
                        "date": today,
                        "clock_in": current_time,
                        "clock_out": "",
                        "status": "Present"
                    }
                )

                messagebox.showinfo(
                    "Identiq",
                    f"{employee_id}\nClock In : {current_time}"
                )

            else:

                attendance_table.update_item(
                    Key={
                        "employee_id": employee_id,
                        "date": today
                    },
                    UpdateExpression="SET clock_out = :t",
                    ExpressionAttributeValues={
                        ":t": current_time
                    }
                )

                messagebox.showinfo(
                    "Identiq",
                    f"{employee_id}\nClock Out : {current_time}"
                )

            return

        elif key == 27:

            cap.release()
            cv2.destroyAllWindows()

            return
        
if __name__ == "__main__":
    recognize()