HTTP service to list the contents of an S3 bucket with Flask and boto3. Returns JSON responses.

# S3 Bucket HTTP Service

## Overview
This project implements a simple HTTP service using Flask and boto3 to interact with an AWS S3 bucket. The service exposes an endpoint to list the contents of the bucket in JSON format. 

## Features
- **GET /list-bucket-content**: Lists the top-level contents of the S3 bucket.
- **GET /list-bucket-content/<path>**: Lists the contents of a specific directory (prefix) in the bucket.

## Example Scenarios
Assume the S3 bucket has the following structure:

|_ dir1 |_ dir2 |_ file1 |_ file2

- **GET /list-bucket-content**  
  Response: `{"content": ["dir1", "dir2", "file1", "file2"]}`

- **GET /list-bucket-content/dir1**  
  Response: `{"content": []}`

- **GET /list-bucket-content/dir2**  
  Response: `{"content": ["file1", "file2"]}`

## Technologies Used
- **Python**: Programming language.
- **Flask**: Web framework for handling HTTP requests.
- **boto3**: AWS SDK for Python, used to interact with S3.
- **Ubuntu**: Operating system for the EC2 instance hosting the service.

## Prerequisites
- AWS account with an S3 bucket created.
- Python 3 installed on the server.
- Virtual environment setup (`python3 -m venv myenv`).

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/s3-bucket-http-service.git
   cd s3-bucket-http-service
