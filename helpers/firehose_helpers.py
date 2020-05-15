import boto3
import json
import os
from dcs_util.helpers.clients import firehose


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


def list_streams():
    return firehose.list_delivery_streams()


def clean_streams():
    streams = list_streams()['DeliveryStreamNames']
    for s in streams:
        firehose.delete_delivery_stream(DeliveryStreamName=s)