import boto3, json, os
from clients import s3

def empty_bucket(Bucket):
    objects = s3.list_objects(Bucket=Bucket)
    if "Contents" in objects:
        for obj in objects['Contents']:
            s3.delete_object(Bucket=bucket_name, Key = obj['Key'])
