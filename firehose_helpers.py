import boto3
import json
import os
from clients import firehose


def create_stream(DeliveryStreamName,
                  BucketName,
                  RoleName,
                  DeliveryStreamType='DirectPut'):
    firehose.create_delivery_stream(
        DeliveryStreamName=DeliveryStreamName,
        DeliveryStreamType="DirectPut",
        S3DestinationConfiguration={
            "RoleARN": "arn:aws:iam::000000000000:role/{}".format(RoleName),
            "BucketARN": "arn:aws:s3:::{}".format(BucketName),
            "BufferingHints": {
                "SizeInMBs": 1,
                "IntervalInSeconds": 60
            },
            "CompressionFormat": "UNCOMPRESSED"
        })
