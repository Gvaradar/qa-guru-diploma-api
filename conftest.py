import pytest
from api.client import ApiClient


@pytest.fixture(scope='session')
def api_client():
    base_url = 'https://fakestoreapi.com'
    return ApiClient(base_url)