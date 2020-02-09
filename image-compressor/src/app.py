import logging

from parsers.event_parser import EventParser
from services.tinify_api_service import TinifyApiService

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info(f'Start event handling event={event}')

    event_parser = EventParser(event)

    if event_parser.is_s3_put_event() and not event_parser.is_invoked_by_lambda():
        tinyfy_api = TinifyApiService(event_parser)

        result = tinyfy_api.compress_and_resize()
        logger.info(f'Result from tinyfy_api.resize_and_compress() = {result}')

        return result

    logger.info('Event is NOT S3 Put Object Event')
    return False
