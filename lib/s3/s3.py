"""S3 connection Class"""
import os
import boto3

class S3Object:
    """Manages s3 connection for data storage"""
    
    def __init__(self):
        self.s3 = boto3.client('s3')
        
    def send_data_to_s3(self, dataset_to_send, s3_bucket, file_prefix):
        """Send data to s3"""
        self.s3.upload_file(Filename=dataset_to_send, Bucket=s3_bucket, Key=file_prefix)
