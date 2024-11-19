from boto3 import client as boto3client
from botocore.config import Config
import json


def call(system_prompt, c):
    bedrock_runtime = boto3client(
        'bedrock-runtime',
        config=Config(region_name="eu-west-3"), aws_access_key_id="AKIA2ZTAOFPDBJGTT7M3",
        aws_secret_access_key="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",
    )

    model_id = 'anthropic.claude-3-sonnet-20240229-v1:0'
    max_tokens = 5000
    um = {"role": "user", "content": c}
    messages = [um]
    response = bedrock_runtime.invoke_model(body=json.dumps(
        {"anthropic_version": "bedrock-2023-05-31","max_tokens": max_tokens,"system": system_prompt,"messages": messages,"temperature": 0.5}
    ), modelId=model_id)
    response_body = json.loads(response.get('body').read())
    return response_body['content'][0]['text']
