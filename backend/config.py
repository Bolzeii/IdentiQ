import boto3

# ---------------- AWS CONFIG ---------------- #

REGION = "ap-south-1"

BUCKET_NAME = "smart-face-attendance-balaji-01"

EMPLOYEE_TABLE = "Employees"

ATTENDANCE_TABLE = "Attendance"

COLLECTION_ID = "employees"

# ---------------- AWS CLIENTS ---------------- #

rekognition = boto3.client(
    "rekognition",
    region_name=REGION
)

s3 = boto3.client(
    "s3",
    region_name=REGION
)

dynamodb = boto3.resource(
    "dynamodb",
    region_name=REGION
)

employee_table = dynamodb.Table(
    EMPLOYEE_TABLE
)

attendance_table = dynamodb.Table(
    ATTENDANCE_TABLE
)