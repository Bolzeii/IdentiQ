# AWS Resources

## Project Name

Identiq

Serverless Smart Attendance System using AWS Cloud

---

## AWS Region

```Bash
ap-south-1
```

---

## AWS Services Used

## 1. Amazon S3

Purpose

- Store employee face images
- Store captured attendance images

Bucket

```Bash
smart-face-attendance-balaji-01
```

Storage Class

```Bash
Standard
```

---

## 2. Amazon Rekognition

Purpose

- Face Registration
- Face Search
- Face Recognition
- Face Collection Management

Collection Name

```Bash
employees
```

Model Version

```Bash
7.0
```

APIs Used

```Bash
CreateCollection

IndexFaces

SearchFacesByImage

ListFaces
```

---

## 3. Amazon DynamoDB

Purpose

Store employee information and attendance records.

### Employees Table

Partition Key

```Bash
employee_id
```

Attributes

- employee_id
- name
- department
- designation
- phone
- email
- image_key

---

### Attendance Table

Partition Key

```Bash
attendance_id
```

Attributes

- attendance_id
- employee_id
- date
- clock_in
- clock_out
- status

---

## 4. AWS IAM

Purpose

Provide secure access to AWS services.

Permissions Required

- AmazonS3FullAccess
- AmazonRekognitionFullAccess
- AmazonDynamoDBFullAccess

---

## 5. boto3 SDK

Purpose

Python SDK for communicating with AWS services.

Services Used

```Bash
boto3.client("s3")

boto3.client("rekognition")

boto3.resource("dynamodb")
```

---

## AWS Architecture

```Bash
               User

                 │

          OpenCV Camera

                 │

          Identiq Desktop

                 │

          Upload Image

                 │

            Amazon S3

                 │

       Amazon Rekognition

                 │

      Search Registered Face

                 │

       Amazon DynamoDB

      Employees + Attendance

                 │

       Attendance Dashboard
```

---

## AWS Resources Summary

| Service | Purpose |
| -------- | --------- |
| Amazon S3 | Store Images |
| Amazon Rekognition | Face Recognition |
| Amazon DynamoDB | Attendance Database |
| AWS IAM | Permissions |
| boto3 | Python SDK |

---

## Security

- IAM Authentication
- Secure AWS APIs
- Cloud-based Storage
- Managed NoSQL Database

---

## Benefits

- Fully Serverless
- Highly Scalable
- Cost Effective
- Secure
- Cloud Native
- Real-Time Attendance
- Easy Deployment

---

## End
