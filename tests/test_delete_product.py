import allure
import pytest


@allure.epic('API тестирование')
@allure.feature('DELETE /products')
class TestDeleteProduct:

    @allure.story('Удаление продукта')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="FakeStoreAPI does not support real deletion")
    def test_delete_product(self, api_client):
        response = api_client.delete('/products/1')
        assert response.status_code == 200

        result = response.json()
        assert result == {}