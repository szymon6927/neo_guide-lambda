import logging
import os

import tinify

from core.exceptions import MissingEnvVariableException
from parsers.event_parser import EventParser
from services.s3_service import S3Service

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class TinifyApiService:
    def __init__(self, event_parser: EventParser):
        self.set_tinfy_api_key()
        self.parser = event_parser

    def set_tinfy_api_key(self) -> None:
        tinify_api_key = os.environ.get('TINIFY_API_KEY')

        if not tinify_api_key:
            raise MissingEnvVariableException('TINIFY_API_KEY is not set')

        tinify.key = tinify_api_key

    def compress_and_resize(self) -> bool:
        try:
            compressed_images = tinify.from_url(self.parser.get_object_url())

            resized_image = compressed_images.resize(method='scale', width=1200)

            S3Service.upload_file(resized_image.to_buffer(), self.parser.get_object_key())

            return True
        except tinify.AccountError as e:
            logger.error('Verify your API key and account limit.')
            logger.exception(f'The error message is: {e.message}')

            return False
        except tinify.ClientError as e:
            logger.error('Check your source image and request options.')
            logger.exception(f'The error message is: {e.message}')

            return False
        except tinify.ServerError as e:
            logger.error('Temporary issue with the Tinify API.')
            logger.exception(f'The error message is: {e.message}')

            return False
        except tinify.ConnectionError as e:
            logger.error('A network connection error occurred.')
            logger.exception(f'The error message is: {e.message}')

            return False
        except Exception as e:
            logger.info('Something else went wrong, unrelated to the Tinify API.')
            logger.exception(f'The error message is: {e}')

            return False
