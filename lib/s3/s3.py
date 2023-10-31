"""S3 connection Class"""
import logging

import boto3
from botocore.exceptions import EndpointConnectionError, NoCredentialsError


class S3Object:
    """Manages s3 connection for data storage"""

    def __init__(self):
        self.s3 = boto3.client("s3")

    def send_data_to_s3(self, dataset_to_send, s3_bucket, file_prefix):
        """Send data to s3"""
        try:
            self.s3.upload_file(
                Filename=dataset_to_send, Bucket=s3_bucket, Key=file_prefix
            )
            logging.info("%s was uploaded successfully", dataset_to_send)
        except NoCredentialsError:
            logging.warning("AWS credentials not found.")
        except EndpointConnectionError:
            logging.warning("Unable to connect to the S3 service endpoint.")
        except Exception as err:
            logging.warning(
                "Error in uploading %s to s3. Error -> %s", dataset_to_send, err
            )
