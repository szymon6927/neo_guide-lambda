import logging
from parsers.event_parser import EventParser

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info(f'Start event handling event={event}')

    event_parser = EventParser(event)
    print(event_parser.get_bucket_name())

    return "ok"
