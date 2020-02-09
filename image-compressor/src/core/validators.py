import logging

from core.constants import FILE_EXTENSIONS

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def is_valid_file_extension(object_key: str) -> bool:
    logger.info(f'Start validating object_key extension for {object_key}')

    for file_extension in FILE_EXTENSIONS:
        if object_key.lower().endswith(file_extension):
            logger.info(f'{object_key} has valid extension!')
            return True

    return False
