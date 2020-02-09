import pytest

from parsers.event_parser import EventParser
from services.s3_service import S3Service
from services.tinify_api_service import TinifyApiService


@pytest.mark.parametrize(
    'object_key, expected_content_type',
    [
        ('mediafiles/test.png', 'image/png'),
        ('mediafiles/test.jpg', 'image/jpeg'),
        ('mediafiles/test.jpeg', 'image/jpeg'),
        ('mediafiles/test.PNG', 'image/png'),
        ('mediafiles/test.JPG', 'image/jpeg'),
        ('mediafiles/test.JPEG', 'image/jpeg'),
    ],
)
def test_s3_service_get_content_type(object_key, expected_content_type):
    assert S3Service.get_content_type(object_key) == expected_content_type


@pytest.mark.parametrize(
    'object_key, expected_content_type', [('mediafiles/test.tiff', 'image/jpeg'), ('mediafiles/test.bmp', 'image/jpeg')]
)
def test_s3_service_get_default_content_type(object_key, expected_content_type):
    assert S3Service.get_content_type(object_key) == expected_content_type


def test_tinify_api_service(s3_put_object_event, mocker):
    event_parser = EventParser(s3_put_object_event)
    tinfiy_service = TinifyApiService(event_parser)

    tinify_from_url_mock = mocker.patch('services.tinify_api_service.tinify.from_url')
    s3_service_mock = mocker.patch('services.tinify_api_service.S3Service.upload_file')

    tinfiy_service.compress_and_resize()

    tinify_from_url_mock.assert_called_once_with(event_parser.get_object_url())
    s3_service_mock.assert_called_once()
