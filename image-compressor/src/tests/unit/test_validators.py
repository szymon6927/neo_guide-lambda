import pytest

from core.validators import is_valid_file_extension


@pytest.mark.parametrize(
    'object_key',
    [
        'mediafiles/test.png',
        'mediafiles/test.jpg',
        'mediafiles/test.jpeg',
        'mediafiles/test.PNG',
        'mediafiles/test.JPG',
        'mediafiles/test.JPEG',
    ],
)
def test_is_valid_file_extension_ok(object_key):
    assert is_valid_file_extension(object_key) is True


@pytest.mark.parametrize(
    'object_key',
    [
        'mediafiles/test.mp3',
        'mediafiles/test.pdf',
        'mediafiles/test.tiff',
        'mediafiles/test.bmp',
        'mediafiles/test.MP3',
        'mediafiles/test.PDF',
    ],
)
def test_is_valid_file_extension_wrong(object_key):
    assert is_valid_file_extension(object_key) is False
