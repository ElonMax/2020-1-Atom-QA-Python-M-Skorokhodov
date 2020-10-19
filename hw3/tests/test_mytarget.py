import pytest


class TestApi:

    @pytest.mark.API
    def test_create(self, api_client):
        segment_id = api_client.create_segment()
        api_client.check_segment(segment_id)

    @pytest.mark.API
    def test_delete(self, api_client):
        segment_id = api_client.create_segment(name='delete_segment')
        api_client.delete_segment(segment_id)
