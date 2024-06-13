import json
import pprint

def handler(event, context):
    print("event:")
    pprint.pp(event)
    print("context:")
    pprint.pp(context)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello world from Lambda!')
    }
