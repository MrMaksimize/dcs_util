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


    s3 = boto3.client('s3', 
                      aws_access_key_id=AWS_KEY_ID, 
                      aws_secret_access_key=AWS_SECRET, 
                      region_name='us-east-1',
                      endpoint_url=endpoints['S3'])

    lambda_client = boto3.client('lambda', 
                      aws_access_key_id=AWS_KEY_ID, 
                      aws_secret_access_key=AWS_SECRET, 
                      region_name='us-east-1',
                      endpoint_url=endpoints['LAMBDA'])