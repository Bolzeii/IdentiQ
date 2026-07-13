# 🎯 Identiq

> Serverless Smart Attendance System using AWS Cloud

![Python](https://img.shields.io/badge/Python-3.12-blue)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-Face%20Recognition-green)
![DynamoDB](https://img.shields.io/badge/DynamoDB-NoSQL-blue)
![Rekognition](https://img.shields.io/badge/Amazon-Rekognition-yellow)

---

## 📌 Overview

Identiq is a cloud-powered smart attendance system that automates employee attendance using facial recognition.

The system captures an employee's face using a webcam, uploads the image to Amazon S3, verifies the identity using Amazon Rekognition, stores attendance records in DynamoDB, and displays real-time attendance statistics through a Python dashboard.

---

## ✨ Features

- Employee Registration
- Face Recognition
- Automatic Attendance
- Amazon Rekognition Integration
- Amazon DynamoDB Storage
- Amazon S3 Image Storage
- Search Employees
- Attendance Dashboard
- Attendance Percentage
- CSV Export
- Real-time Statistics

---

## 🏗 AWS Services Used

- Amazon S3
- Amazon Rekognition
- Amazon DynamoDB
- AWS IAM
- boto3 SDK

---

## 💻 Tech Stack

Python

CustomTkinter

OpenCV

AWS boto3

Amazon Rekognition

Amazon DynamoDB

Amazon S3

---

## 📂 Project Structure

backend/

attendance_dashboard.py

register_employee.py

recognize_face.py

create_collection.py

config.py

lambda/

attendance_processor/

register_face/

weekly_summary/

docs/

README.md

Deployment_Guide.md

Cost_Estimation.xlsx

---

## 🚀 Installation

Install dependencies

pip install boto3

pip install opencv-python

pip install customtkinter

pip install pandas

Configure AWS Credentials

aws configure

Run

python backend/attendance_dashboard.py

---

## 📷 Workflow

Capture Face

↓

Upload to Amazon S3

↓

Amazon Rekognition

↓

Match Employee

↓

Store Attendance in DynamoDB

↓

Update Dashboard

---

## 📊 Dashboard

✔ Employee Count

✔ Present Today

✔ Absent Today

✔ Attendance %

✔ Search

✔ Export CSV

---

## 🔮 Future Enhancements

Mobile App

QR Attendance

Live Face Recognition

Email Notifications

Analytics Dashboard

Multi-office Support

---

## 👨‍💻 Developer

Balaji G

F13 Technologies

Project Name

IdentiQ
