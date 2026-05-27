import os
import pytest
from dotenv import load_dotenv
from api.client import ApiClient

load_dotenv()


@pytest.fixture(scope='session')
def api_client():
    base_url = os.getenv('API_BASE_URL', 'https://fakestoreapi.com')
    return ApiClient(base_url)