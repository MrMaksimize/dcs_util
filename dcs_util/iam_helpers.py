import boto3
import json
import os

from dcs_util.clients import iam

policy = {
    "Version":
    "2012-10-17",
    "Statement": [{
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
    }]
}

policies = {
    "S3_FULL": "AmazonS3FullAccess",
    "LAMBDA_FULL": "AWSLambdaFullAccess",
    "KINESIS_FULL": "AmazonKinesisFullAccess",
    "KINESIS_FIREHOSE_FULL": "AmazonKinesisFirehoseFullAccess",
    "KINESIS_ANALYTICS_FULL": "AmazonKinesisAnalyticsFullAccess",
    "CLOUD_TRAIL_FULL": "AWSCloudTrailFullAccess",
    "CLOUD_WATCH_FULL": "CloudWatchFullAccess"
}


def clean_roles():
    for role in iam.list_roles()['Roles']:
        role_name = role['RoleName']
        attached_policies = iam.list_attached_role_policies(
            RoleName=role_name)['AttachedPolicies']
        for p in attached_policies:
            iam.detach_role_policy(RoleName=role_name,
                                   PolicyArn=p['PolicyArn'])
        iam.delete_role(RoleName=role['RoleName'])


def make_role(RoleName):
    iam.create_role(RoleName=RoleName,
                    AssumeRolePolicyDocument=json.dumps(policy))
    for idx, p in policies.items():
        iam.attach_role_policy(RoleName=RoleName,
                               PolicyArn="arn:aws:iam::aws:policy/" + p)
