"""Simple AWS Lambda handler for the Experiment 4 serverless requirement."""
import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "message": "Hello from AWS Lambda",
            "project": "CI/CD Pipeline Demonstration"
        })
    }
