from pprint import pprint
import boto3
from botocore.exceptions import ClientError

def put_counter(id, counter_value, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
    
    table = dynamodb.Table('VisitorCounterDB')
    response = table.put_item(
        Item={
            'id': id,
            'counter_value': counter_value
        }
    )
    
    return response
    
if __name__ == '__main__':
    counter_resp = put_counter('counter', 0)
    print('Put counter successfully')
    pprint(counter_resp, sort_dicts=False)