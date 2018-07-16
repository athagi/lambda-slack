import requests
import os

def main(webhookUrl):
    # print("hello world")
    data = [
    ('payload', '{"channel": "#general", "text": "This is posted to #general and comes from a bot named webhookbot. test"}'),
    ]

    response = requests.post(webhookUrl, data=data, verify=False)

    return response.status_code
    
def lambda_handler(event, context):
    webhookUrl = os.environ['WEBHOOK_URL']
    main(webhookUrl)

if __name__ == '__main__':
    lambda_handler("","")