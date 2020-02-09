import logging

import boto3
from botocore.exceptions import ClientError

from core.constants import BUCKET_NAME

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class S3Service:
    @staticmethod
    def upload_file(file, object_key):
        logging.info('Start uploading file to S3 bucket')

        try:
            s3 = boto3.client('s3')
            s3.put_object(Bucket=BUCKET_NAME, Key=object_key, Body=file)
        except ClientError as e:
            logger.exception(f'Something went wrong during "upload_file", {e}')
            raise
