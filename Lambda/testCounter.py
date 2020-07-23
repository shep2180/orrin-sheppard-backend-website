from pprint import pprint
import unittest
import boto3
from botocore.exceptions import ClientError
from moto import mock_dynamodb2

@mock_dynamodb2
class TestDatabaseFunctions(unittest.TestCase):
    def setUp(self):
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        
        from createCounterTable import create_counter_table
        self.table = create_counter_table(self.dynamodb)
        
    def tearDown(self):
        self.table.delete()
        self.dynamodb = None
    
    def test_table_exists(self):
        def test_table_exists():
            self.assertIn('VisitorCounterDB')
            
    def test_put_counter(self):
        from putCounter import put_counter
        
        result = put_counter('counter', 0, self.dynamodb)
        
        self.assertEqual(200, result['ResponseMetadata']['HTTPStatusCode'])
        
    def test_get_counter(self):
        from putCounter import put_counter
        from getCounter import get_counter
        
        put_counter('counter', 0, self.dynamodb)
        result = get_counter('counter', 0, self.dynamodb)
        
        self.assertEqual('counter', result['id'])
        self.assertEqual(0, result['counter_value'])
        
    def test_increment_counter(self):
        from app import addVisitor
        from putCounter import put_counter
        from getCounter import get_counter
        
        put_counter('counter', 0, self.dynamodb)
        var1 = get_counter('counter', 0, self.dynamodb)
        var2 = addVisitor(var1['counter_value'])
        
        self.assertEqual(var1['counter_value'] + 1, var2, self.dynamodb)
    
if __name__ == '__main__':
    unittest.main()