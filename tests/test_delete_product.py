import allure
from api.helpers import assert_status_code


@allure.epic('API тестирование')
@allure.feature('DELETE /products')
class TestDeleteProduct:

    @allure.story('Удаление продукта')
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_product(self, api_client):
        response = api_client.delete('/products/1')
        assert_status_code(response)

        result = response.json()
        assert result == {}