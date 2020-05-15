import boto3
import json
import os
from zipfile import ZipFile
from dcs.util.clients import lambda_client


def create_lambda_zip(function_name):
    original_wd = os.getcwd()
    # Change into function directory
    os.chdir("./{}".format(function_name))
    with ZipFile("../{}.zip".format(function_name), 'w') as z:
        for file in os.listdir("."):
            z.write("./{}".format(file))
    # Change back into function directory
    os.chdir(original_wd)


def create_lambda(function_name, handler_name):
    print("Compressing code for {} into zipfile for upload".format(
        function_name))

    create_lambda_zip(function_name)

    with open("./{}.zip".format(function_name), 'rb') as f:
        zipped_code = f.read()
    print("Creating {} function on AWS".format(function_name))
    lambda_client.create_function(
        FunctionName=function_name,
        Runtime='python3.8',
        Role='role',
        Handler="lambda_function.{}".format(handler_name),
        Code=dict(ZipFile=zipped_code))


def invoke_function_and_get_message(function_name, payload):
    print("Invoking lambda function {}".format(function_name))
    print("Lambda function return:")
    response = lambda_client.invoke(FunctionName=function_name,
                                    InvocationType='RequestResponse',
                                    Payload=json.dumps(payload))
    return response['Payload'].read().decode('utf-8')


def clean_lambdas(Except=None):
    print("Cleaning up runtime")
    lambdas = lambda_client.list_functions()['Functions']
    if len(lambdas) > 0:
        for fxn in lambdas:
            fname = fxn['FunctionName']
            if (Except != fname):
                lambda_client.delete_function(FunctionName=fname)
            if os.path.isfile("./{}.zip".format(fname)):
                os.remove("./{}.zip".format(fname))
