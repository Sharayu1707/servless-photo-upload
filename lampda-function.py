import json
import boto3
import base64
import uuid

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = "serverlessphotouploadbucket"
    
    # Example file details
    file_name = f"{uuid.uuid4()}.jpg"
    file_content = base64.b64decode(event['body'])
    
    # Upload file to S3
    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=file_content,
        ContentType='image/jpeg',
        ACL='public-read'  # <-- makes image public automatically
    )
    
    file_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': '✅ File uploaded successfully!',
            'file_url': file_url
        })
    }
