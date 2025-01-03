import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    """
    Increments the 'visitor_count' value in a DynamoDB table by 1.

    Args:
        event: AWS Lambda event object.
        context: AWS Lambda context object.

    Returns:
        A dictionary containing the updated 'visitor_count' value.
    """

    response = table.update_item(
        Key={'id': 'visitor_count'},
        UpdateExpression="set visitor_count = if_not_exists(visitor_count, :zero) + :incr",
            ExpressionAttributeValues={
                ':zero': 0,
                ':incr': 1
            },
        ReturnValues='UPDATED_NEW'
    )
    
    visitor_count = response['Attributes']['visitor_count']
    print(f"Visitor count: {visitor_count}")
    
    return {
        'statusCode': 200,
        'body': json.dumps({'visitor_count': str(visitor_count)})
    }