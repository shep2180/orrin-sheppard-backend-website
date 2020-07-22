import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ResumeWebsiteCounter')

def addVisitor():
    resp = table.get_item(Key={'id': 'counter'})
    value = resp['Item']['counter_value'] + 1
    resp = table.update_item(Key={'id':'counter'}, UpdateExpression='set counter_value=:value', ExpressionAttributeValues={':value': value})

def lambda_handler(event, context):
    
    addVisitor()
    
    resp2 = table.get_item(Key={'id':'counter'})
    
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers" : "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
        },
        "body": json.dumps({
            "visitorCount": int(resp2["Item"]['counter_value'])
        })
    }
    
    return response