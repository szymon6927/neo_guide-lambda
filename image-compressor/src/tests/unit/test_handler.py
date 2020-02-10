from app import lambda_handler


def test_lambda_handler_ok(s3_put_object_event, mocker):
    tinify_api_service_mock = mocker.patch('services.tinify_api_service.TinifyApiService.compress_and_resize')
    tinify_api_service_mock.return_value = True

    result = lambda_handler(s3_put_object_event, '')

    assert result is True


def test_lambda_handler_when_tinify_service_wrong(s3_put_object_event, mocker):
    tinify_api_service_mock = mocker.patch('services.tinify_api_service.TinifyApiService.compress_and_resize')
    tinify_api_service_mock.return_value = False

    result = lambda_handler(s3_put_object_event, '')

    assert result is False


def test_handler_when_event_not_s3_put_object(s3_delete_object_event):
    result = lambda_handler(s3_delete_object_event, '')

    assert result is False
