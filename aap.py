from flask import Flask, jsonify
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

app = Flask(__name__)

# Replace with your bucket name
BUCKET_NAME = "my-s3-bucket2024 "

# Initialize the S3 client
s3_client = boto3.client("s3")


def list_bucket_content(path=""):
    try:
        # Use S3 paginator to list objects
        paginator = s3_client.get_paginator("list_objects_v2")
        response_iterator = paginator.paginate(Bucket=BUCKET_NAME, Prefix=path, Delimiter='/')

        content = []

        for response in response_iterator:
            # Add directories (common prefixes) to content
            if "CommonPrefixes" in response:
                content.extend([prefix["Prefix"] for prefix in response["CommonPrefixes"]])

            # Add files (keys) to content
            if "Contents" in response:
                content.extend([obj["Key"] for obj in response["Contents"] if obj["Key"] != path])

        # Filter and clean up the response content for the path
        cleaned_content = [item[len(path):] for item in content if item.startswith(path)]
        return {"content": cleaned_content}
    except (NoCredentialsError, PartialCredentialsError):
        return {"error": "AWS credentials not found or incomplete"}, 500
    except Exception as e:
        return {"error": str(e)}, 500


@app.route("/list-bucket-content", defaults={"path": ""})
@app.route("/list-bucket-content/<path:path>")
def get_bucket_content(path):
    # Add trailing slash if path is a folder
    if path and not path.endswith('/'):
        path += '/'
    result = list_bucket_content(path)
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
