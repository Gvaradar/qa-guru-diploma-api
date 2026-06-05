import allure
from jsonschema import validate

from api.schemas import product_request_schema


@allure.epic('API тестирование')
@allure.feature('POST /products')
class TestPostProduct:

    @allure.story('Создание продукта')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('smoke', 'positive')
    def test_create_product(self, api_client, sample_product):
        response = api_client.post('/products', json=sample_product.model_dump())
        assert response.status_code == 201

        created = response.json()
        assert created['title'] == sample_product.title
        assert created['price'] == sample_product.price
        assert 'id' in created

        validate(instance=created, schema=product_request_schema)
