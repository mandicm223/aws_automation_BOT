import boto3
from botocore.exceptions import ClientError

client = boto3.client('s3')

def run():
    try:
        bucket_name=input("Please enter name of your bucket: ")
        key = input("Please enter key of your file.")
        filename=input("Please sign  name to file that you want to download")

        client.download_file(Bucket=bucket_name , Key=key , Filename=filename ,)
        print(f"{key} is downloaded")
        print(f"{filename} is placed into your dir.")
    except ClientError as e:
        print(e)