import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCounterDB')

def addVisitor(value):
    return value + 1

def lambda_handler(event, context):
    var1 = table.get_item(Key={'id':'counter'})
    
    value = addVisitor(var1['Item']['counter_value'])
    
    var2 = table.update_item(Key={'id':'counter'}, UpdateExpression='set counter_value=:value', ExpressionAttributeValues={':value': value})
    
    var3 = table.get_item(Key={'id':'counter'})
    
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers" : "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
        },
        "body": json.dumps({
            "visitorCount": int(var3["Item"]['counter_value'])
        })
    }
    
    return response