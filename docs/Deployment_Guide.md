# Deployment Guide

## IdentiQ

### Serverless Smart Attendance System using AWS Cloud

---

## Prerequisites

Before running the application, ensure the following software is installed:

- Python 3.11 or later
- Git
- Visual Studio Code
- AWS CLI
- pip

---

## Step 1 - Clone the Project

```bash
git clone https://github.com/yourusername/identiq.git
cd identiq
```

---

## Step 2 - Install Python Packages

```bash
pip install boto3
pip install pandas
pip install customtkinter
pip install opencv-python
pip install pillow
```

Or simply run:

```bash
pip install -r requirements.txt
```

---

## Step 3 - Configure AWS CLI

```bash
aws configure
```

Provide:

- AWS Access Key
- AWS Secret Key
- Region

```bash
ap-south-1
```

---

## Step 4 - Create AWS Resources

## Amazon S3

Create a bucket.

Example

```Bash
identiq-attendance-images
```

Store captured employee images here.

---

## Amazon Rekognition

Run

```bash
python backend/create_collection.py
```

This creates the Rekognition collection used to store employee face embeddings.

---

## Amazon DynamoDB

Create two tables.

### Employees

Partition Key

```Bash
employee_id
```

### Attendance

Partition Key

```Bash
attendance_id
```

---

## Step 5 - Register Employees

Run

```bash
python backend/register_employee.py
```

This process:

- Opens the webcam
- Captures employee face
- Uploads image to Amazon S3
- Indexes the face into Amazon Rekognition
- Stores employee information in DynamoDB

---

## Step 6 - Start Dashboard

```bash
python backend/attendance_dashboard.py
```

Dashboard Features

- Register Employee
- Take Attendance
- Search Employee
- Refresh Dashboard
- Export CSV

---

## Step 7 - Take Attendance

Click

```Bash
Take Attendance
```

The system will

- Capture image
- Upload to Amazon S3
- Search the Rekognition collection
- Retrieve employee details
- Mark attendance in DynamoDB
- Refresh dashboard

---

## Project Workflow

```Bash
Capture Face
      │
      ▼
Upload Image to Amazon S3
      │
      ▼
Amazon Rekognition
      │
      ▼
Employee Identified
      │
      ▼
Amazon DynamoDB
      │
      ▼
Attendance Dashboard
```

---

## Troubleshooting

## Webcam not opening

- Check camera permissions
- Close other applications using the webcam

---

## AWS Authentication Error

Run

```bash
aws configure
```

again.

---

## Collection Not Found

Run

```bash
python backend/create_collection.py
```

---

## No Face Matched

Possible reasons

- Employee not registered
- Poor lighting
- Face not clearly visible

---

## S3 Upload Failed

Check

- Internet connection
- Bucket name
- IAM permissions

---

## AWS Services Used

- Amazon S3
- Amazon Rekognition
- Amazon DynamoDB
- AWS IAM
- boto3 SDK

---

## End

Identiq is now ready for deployment.
