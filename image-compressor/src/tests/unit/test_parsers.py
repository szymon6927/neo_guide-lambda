import pytest

from core.exceptions import BusinessLogicException
from parsers.event_parser import EventParser


def test_event_parser_is_s3_put_event(s3_put_object_event):
    parser = EventParser(s3_put_object_event)

    assert parser.is_s3_put_event() is True


def test_event_parser_is_not_s3_put_event(s3_delete_object_event):
    parser = EventParser(s3_delete_object_event)

    assert parser.is_s3_put_event() is False


def test_event_parser_get_bucket_name(s3_put_object_event):
    parser = EventParser(s3_put_object_event)
    bucket_name = parser.get_bucket_name()

    assert bucket_name == 'example-bucket'


def test_event_parser_get_bucket_name_when_no_bucket():
    parser = EventParser({})
    bucket_name = parser.get_bucket_name()

    assert bucket_name is None


def test_event_parser_get_object_key(s3_put_object_event):
    parser = EventParser(s3_put_object_event)
    object_key = parser.get_object_key()

    assert object_key == 'test/key.jpg'


def test_event_parser_get_object_key_when_no_object_key():
    parser = EventParser({})
    object_key = parser.get_object_key()

    assert object_key is None


def test_event_parser_get_object_url(s3_put_object_event):
    parser = EventParser(s3_put_object_event)
    object_url = parser.get_object_url()

    assert object_url == 'https://neo-guide-be.s3.eu-central-1.amazonaws.com/test/key.jpg'


def test_event_parser_get_object_url_when_no_object_key():
    parser = EventParser({})

    with pytest.raises(BusinessLogicException):
        parser.get_object_url()


def test_event_parser_is_invoked_by_lambda(s3_put_object_event):
    parser = EventParser(s3_put_object_event)

    assert parser.is_invoked_by_lambda() is False


def test_event_parser_is_invoked_by_lambda_when_it_is(s3_put_object_event_invoked_by_lambda_itself):
    parser = EventParser(s3_put_object_event_invoked_by_lambda_itself)

    assert parser.is_invoked_by_lambda() is True
