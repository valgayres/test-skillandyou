from boto3 import client as boto3client
from botocore.config import Config
import json


def call_bedrock(system_prompt, content):
    config = Config(region_name="eu-west-3")

    bedrock_runtime = boto3client(
        'bedrock-runtime',
        config=config, aws_access_key_id="COPY_KEY_HERE",
        aws_secret_access_key="COPY_KEY_HERE",
    )

    model_id = 'anthropic.claude-3-sonnet-20240229-v1:0'
    max_tokens = 5000
    user_message = {"role": "user", "content": content}
    messages = [user_message]
    body = json.dumps(
        {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": max_tokens,
            "system": system_prompt,
            "messages": messages,
            "temperature": 0.5,
        }
    )
    response = bedrock_runtime.invoke_model(body=body, modelId=model_id)
    response_body = json.loads(response.get('body').read())
    return response_body['content'][0]['text']
