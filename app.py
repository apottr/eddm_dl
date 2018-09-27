import requests
import boto3

client = boto3.client('sns')
print(client.list_topics())