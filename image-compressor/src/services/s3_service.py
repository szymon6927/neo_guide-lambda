import logging

import boto3
from botocore.exceptions import ClientError

from core.constants import BUCKET_NAME

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class S3Service:
    @staticmethod
    def upload_file(file: bytes, object_key: str) -> None:
        logging.info('Start uploading file to S3 bucket')

        try:
            s3 = boto3.client('s3')
            s3.put_object(
                Bucket=BUCKET_NAME, Key=object_key, Body=file, ContentType=S3Service.get_content_type(object_key)
            )
        except ClientError as e:
            logger.exception(f'Something went wrong during "upload_file", {e}')
            raise

    @staticmethod
    def get_content_type(object_key: str) -> str:
        if object_key.lower().endswith('jpg') or object_key.lower().endswith('jpeg'):
            return 'image/jpeg'

        if object_key.lower().endswith('png'):
            return 'image/png'

        return 'image/jpeg'
