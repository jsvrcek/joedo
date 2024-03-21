import boto3
import os

s3_client = boto3.client(
    's3',
    endpoint_url=os.getenv('AWS_S3_ENDPOINT_URL'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_S3_REGION_NAME'),
    use_ssl=False if 'minio' in os.getenv('AWS_S3_ENDPOINT_URL') else True
)


def create_bucket():
    bucket_name = os.getenv('AWS_STORAGE_BUCKET_NAME')
    try:
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' created successfully.")
    except s3_client.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            print(f"Bucket '{bucket_name}' already exists.")
        else:
            raise e


if __name__ == "__main__":
    create_bucket()
