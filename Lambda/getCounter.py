from pprint import pprint
import boto3
from botocore.exceptions import ClientError

def get_counter(id, counter_value, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    
    table = dynamodb.Table('VisitorCounterDB')
    
    try:
        response = table.get_item(Key={'id': id, 'counter_value': counter_value})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']
    
if __name__ == '__main__':
    counter = get_counter('counter', 0)
    if counter:
        print('Get counter successful')
        pprint(counter, sort_dicts=False)