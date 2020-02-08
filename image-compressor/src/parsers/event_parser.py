from core.types import Event


class EventParser:
    def __init__(self, event: dict):
        self.event: Event = event

    def is_s3_put_event(self):
        return self.event.get('Records')[0].get('eventName') == 'ObjectCreated:Put'

    def get_bucket_name(self):
        return self.event.get('Records')[0].get('s3').get('bucket').get('name')
