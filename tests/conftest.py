import os

import pytest
from dotenv import load_dotenv

from api.client import ApiClient
from models.product import Product, UpdatedProduct

load_dotenv()


@pytest.fixture(scope='session')
def api_client():
    base_url = os.getenv('API_BASE_URL', 'https://fakestoreapi.com')
    return ApiClient(base_url)


@pytest.fixture
def sample_product():
    return Product(
        title="Test Product",
        price=99.99,
        description="This is a test product for diploma",
        category="electronic",
        image="https://via.placeholder.com/300"
    )


@pytest.fixture
def updated_product_data():
    return UpdatedProduct(
        id=1,
        title="Updated Backpack",
        price=129.95,
        description="Updated description",
        category="men's clothing",
        image="https://via.placeholder.com/300"
    )
