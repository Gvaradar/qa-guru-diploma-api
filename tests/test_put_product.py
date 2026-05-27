import allure
from jsonschema import validate
from api.schemas import product_schema
from api.helpers import assert_status_code


@allure.epic('API тестирование')
@allure.feature('PUT /products')
class TestPutProduct:

    @allure.story('Обновление продукта')
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_product(self, api_client):
        updated_data = {
            "id": 1,
            "title": "Updated Backpack",
            "price": 129.95,
            "description": "Updated description",
            "category": "men's clothing",
            "image": "https://via.placeholder.com/300"
        }

        response = api_client.put('/products/1', json=updated_data)
        assert_status_code(response)

        result = response.json()
        assert result['title'] == "Updated Backpack"
        assert result['price'] == 129.95

        validate(instance=result, schema=product_schema)