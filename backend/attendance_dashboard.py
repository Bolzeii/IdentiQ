import subprocess
import os
import pandas as pd
from tkinter import filedialog, messagebox
import boto3
import customtkinter as ctk
from tkinter import ttk
from datetime import datetime

# ---------------- AWS ---------------- #

REGION = "ap-south-1"
TABLE_NAME = "Attendance"
EMPLOYEE_TABLE = "Employees"

dynamodb = boto3.resource("dynamodb", region_name=REGION)

table = dynamodb.Table(TABLE_NAME)
employee_table = dynamodb.Table(EMPLOYEE_TABLE)

# ---------------- UI ---------------- #

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Identiq")
app.geometry("1100x800")
app.resizable(False, False)

title = ctk.CTkLabel(
    app,
    text="Identiq",
    font=("Arial", 24, "bold")
)
title.pack(pady=10)

subtitle = ctk.CTkLabel(
    app,
    text="Serverless Smart Attendance System using AWS Cloud",
    font=("Arial",14)
)

subtitle.pack(pady=3)

today_label = ctk.CTkLabel(
    app,
    text=f"Today's Date : {datetime.now().strftime('%Y-%m-%d')}",
    font=("Arial",16)
)
today_label.pack()

search_var = ctk.StringVar()

search_entry = ctk.CTkEntry(
    app,
    textvariable=search_var,
    width=300,
    placeholder_text="Search Employee Name..."
)
search_entry.pack(pady=10)

# ---------------- STATISTICS ---------------- #

stats_frame = ctk.CTkFrame(app)
stats_frame.pack(fill="x", padx=20, pady=10)

employees_label = ctk.CTkLabel(
    stats_frame,
    text="👥 Total Employees\n0",
    font=("Arial",16,"bold")
)
employees_label.grid(row=0,column=0,padx=25,pady=10)

present_label = ctk.CTkLabel(
    stats_frame,
    text="✅ Present Today\n0",
    font=("Arial",16,"bold")
)
present_label.grid(row=0,column=1,padx=25,pady=10)

absent_label = ctk.CTkLabel(
    stats_frame,
    text="❌ Absent Today\n0",
    font=("Arial",16,"bold")
)
absent_label.grid(row=0,column=2,padx=25,pady=10)

percentage_label = ctk.CTkLabel(
    stats_frame,
    text="📊 Attendance %\n0%",
    font=("Arial",16,"bold")
)
percentage_label.grid(row=0,column=3,padx=25,pady=10)



tree = ttk.Treeview(
    app,
    columns=("Employee", "Date", "Clock In", "Clock Out", "Status"),
    show="headings",
    height=18
)

tree.heading("Employee", text="Employee Name")
tree.heading("Date", text="Date")
tree.heading("Clock In", text="Clock In")
tree.heading("Clock Out", text="Clock Out")
tree.heading("Status", text="Status")

tree.column("Employee", width=220)
tree.column("Date", width=150)
tree.column("Clock In", width=150)
tree.column("Clock Out", width=150)
tree.column("Status", width=150)



# ---------------- FUNCTIONS ---------------- #

def get_employee_name(employee_id):

    response = employee_table.get_item(
        Key={
            "employee_id": employee_id
        }
    )

    if "Item" in response:
        return response["Item"]["name"]

    return employee_id


def load_data():

    for row in tree.get_children():
        tree.delete(row)

    response = table.scan()

    items = response.get("Items", [])

    employee_response = employee_table.scan()
    employees = employee_response.get("Items", [])

    total_employees = len(employees)

    today = datetime.now().strftime("%Y-%m-%d")

    present_today = len([
        item for item in items
        if item.get("date") == today
    ])

    absent_today = max(0, total_employees - present_today)

    percentage = (
        round((present_today / total_employees) * 100, 1)
        if total_employees else 0
    )

    employees_label.configure(
        text=f"👥 Total Employees\n{total_employees}"
    )

    present_label.configure(
        text=f"✅ Present Today\n{present_today}"
    )

    absent_label.configure(
        text=f"❌ Absent Today\n{absent_today}"
    )

    percentage_label.configure(
        text=f"📊 Attendance %\n{percentage}%"
    )

    search_text = search_var.get().lower()

    for item in items:

        employee_name = get_employee_name(
            item.get("employee_id", "")
        )

        if search_text != "":
            if search_text not in employee_name.lower():
                continue

        tree.insert(
            "",
            "end",
            values=(
                employee_name,
                item.get("date", ""),
                item.get("clock_in", ""),
                item.get("clock_out", ""),
                item.get("status", "")
            )
        )

def export_csv():

    response = table.scan()

    items = response.get("Items", [])

    if not items:
        messagebox.showwarning(
            "No Data",
            "No attendance records found!"
        )
        return

    for item in items:
        item["employee_name"] = get_employee_name(
            item["employee_id"]
        )

    df = pd.DataFrame(items)

    columns = [
        "employee_name",
        "employee_id",
        "date",
        "clock_in",
        "clock_out",
        "status"
    ]

    df = df[columns]

    filename = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv")],
        initialfile="Identiq_Attendance_Report.csv.csv"
    )

    if filename:

        df.to_csv(filename, index=False)

        messagebox.showinfo(
            "Success",
            "Attendance exported successfully!"
        )


def take_attendance():

    try:

        process = subprocess.Popen(
            ["python", os.path.join("backend", "recognize_face.py")]
        )

        process.wait()

        load_data()

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )

def register_employee():

    try:

        process = subprocess.Popen(
            ["python", os.path.join("backend", "register_employee.py")]
        )

        process.wait()

        load_data()

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )

# ---------------- BUTTONS ---------------- #

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=10)

refresh_btn = ctk.CTkButton(
    button_frame,
    text="🔄 Refresh",
    command=load_data,
    width=170
)
refresh_btn.grid(row=0, column=0, padx=10)

export_btn = ctk.CTkButton(
    button_frame,
    text="📄 Export CSV",
    command=export_csv,
    fg_color="orange",
    width=170
)
export_btn.grid(row=0, column=1, padx=10)

attendance_btn = ctk.CTkButton(
    button_frame,
    text="📷 Take Attendance",
    command=take_attendance,
    fg_color="green",
    width=170
)
attendance_btn.grid(row=0, column=2, padx=10)

register_btn = ctk.CTkButton(
    button_frame,
    text="➕ Register Employee",
    command=register_employee,
    fg_color="blue",
    width=170
)
register_btn.grid(row=0, column=3, padx=10)

tree.pack(fill="both", expand=True, padx=20, pady=20)

# ---------------- START ---------------- #

load_data()

search_var.trace_add(
    "write",
    lambda *args: load_data()
)

app.mainloop()