import boto3, json, os
from dcs_util.clients import *


def empty_bucket(Bucket):
    objects = s3.list_objects(Bucket=Bucket)
    if "Contents" in objects:
        for obj in objects['Contents']:
            s3.delete_object(Bucket=Bucket, Key=obj['Key'])


def delete_bucket(Bucket):
    empty_bucket(Bucket)
    s3.delete_bucket(Bucket=Bucket)


def create_bucket(Bucket):
    s3.create_bucket(Bucket=Bucket)