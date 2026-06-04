import allure
from jsonschema import validate
from api.schemas import product_schema


@allure.epic('API тестирование')
@allure.feature('PUT /products')
class TestPutProduct:

    @allure.story('Обновление продукта')
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_product(self, api_client, updated_product_data):
        response = api_client.put('/products/1', json=updated_product_data.model_dump())
        assert response.status_code == 200

        result = response.json()
        assert result['title'] == updated_product_data.title
        assert result['price'] == updated_product_data.price

        validate(instance=result, schema=product_schema)