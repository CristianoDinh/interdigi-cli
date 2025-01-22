from argparse import ArgumentParser, Namespace
import boto3, os

parser = ArgumentParser()
#parser.usage
parser.prog = "./download.exe"
parser.description = "Download your required file from Cloud Object Storage AWS-S3 -> Local storage"
parser.add_argument("bucket_file_name", help = ":Name of the file to be downloaded", type = str)
parser.add_argument("bucket_source_name", help = ":S3 bucket source of file to be downloaded", type = str)
parser.add_argument("new_file_path", help = ":Path and name of the downloaded file", type = str)

args : Namespace = parser.parse_args()
s3 = boto3.client('s3', region_name='ap-southeast-1')

BUCKET_FILE = args.bucket_file_name
BUCKET_NAME = args.bucket_source_name
NEW_FILE_PATH = args.new_file_path

# Extract directory path from the file path
directory_path = os.path.dirname(NEW_FILE_PATH)

try:
    # Create the directory if it doesn't exist
    if directory_path and not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Created new directory: {directory_path}")

    with open(NEW_FILE_PATH, "wb") as file:
        s3.download_fileobj(BUCKET_NAME, BUCKET_FILE, file)
        print(f"Downloaded new file '{NEW_FILE_PATH}' from bucket '{BUCKET_NAME}'")
except Exception as e:
    print(f"Failed to download file from bucket '{BUCKET_NAME}'\nReason: {e}")

