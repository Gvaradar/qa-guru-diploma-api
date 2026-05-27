import allure
from jsonschema import validate
from api.schemas import product_request_schema


@allure.epic('API тестирование')
@allure.feature('POST /products')
class TestPostProduct:

    @allure.story('Создание продукта')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('smoke', 'positive')
    def test_create_product(self, api_client):
        new_product = {
            "title": "Test Product",
            "price": 99.99,
            "description": "This is a test product for diploma",
            "category": "electronic",
            "image": "https://via.placeholder.com/300"
        }

        response = api_client.post('/products', json=new_product)

        assert response.status_code == 200

        created = response.json()
        assert created['title'] == new_product['title']
        assert created['price'] == new_product['price']
        assert 'id' in created

        validate(instance=created, schema=product_request_schema)