import boto3
import json
import os

from clients import iam

policy = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
            "lambda.amazonaws.com",
            "s3.amazonaws.com",
            "kinesis.amazonaws.com",
            "firehose.amazonaws.com",
            "kinesisanalytics.amazonaws.com",
        ]
      },
      "Action": "sts:AssumeRole"
    }
  ]
}

policies = {
    "S3_FULL": "AmazonS3FullAccess"
    "LAMBDA_FULL": "AWSLambdaFullAccess"
    "KINESIS_FULL": "AmazonKinesisFullAccess"
    "KINESIS_FIREHOSE_FULL": "AmazonKinesisFirehoseFullAccess"
    "KINESIS_ANALYTICS_FULL": "AmazonKinesisAnalyticsFullAccess"
    "CLOUD_TRAIL_FULL": "AWSCloudTrailFullAccess"
    "CLOUD_WATCH_FULL": "CloudWatchFullAccess"
}


def clean_roles():
    for role in iam.list_roles()['Roles']:
        for p in policies:
            iam.detach_role_policy(role['RoleName'], 
                                   policyArn = "arn:aws:iam::aws:policy/" + p)
        delete_role(role['RoleName'])


def make_role(RoleName, policies):
    iam.create_role(RoleName=RoleName, AssumeRolePolicyDocument=json.dumps(policy))
    for p in policies:
        iam.attach_role_policy(RoleName, 
            policyArn = "arn:aws:iam::aws:policy/" + p)
        


