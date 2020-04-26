# PLEASE DO NOT EDIT
# run_lambda.py
# These are helper utilities for working with Lambda functins
import boto3
import json
import os
from zipfile import ZipFile

#localstack
AWS_ACCT_ID = "000000000000"
AWS_KEY_ID = "NUNYA"
AWS_SECRET = "BIZNESS"

endpoints = {
    "S3": "http://localhost:4572",
    "FIREHOSE": "http://localhost:4573",
    "IAM": "http://localhost:4593",
    "LAMBDA": "http://localhost:4574",
    "KINESIS": "http://localhost:4568",
}

clients = {}

for idx, row in endpoints.items():

    clients[idx.lower()] = boto3.client(idx.lower(),
                                        aws_access_key_id=AWS_KEY_ID,
                                        aws_secret_access_key=AWS_SECRET,
                                        region_name='us-east-1',
                                        endpoint_url=endpoints[idx])

s3, firehose, iam, lambda_client, kinesis = clients.values()