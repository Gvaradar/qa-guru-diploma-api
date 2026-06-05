import allure
from jsonschema import validate

from api.schemas import product_schema, products_list_schema


@allure.epic('API тестирование')
@allure.feature('GET /products')
class TestGetProducts:

    @allure.story('Получение всех продуктов')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('smoke', 'positive')
    def test_get_all_products(self, api_client):
        response = api_client.get('/products')
        assert response.status_code == 200

        products = response.json()
        assert isinstance(products, list)
        assert len(products) > 0
        validate(instance=products, schema=products_list_schema)

    @allure.story('Получение одного продукта')
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_single_product(self, api_client):
        response = api_client.get('/products/1')
        assert response.status_code == 200

        product = response.json()
        assert product['id'] == 1
        validate(instance=product, schema=product_schema)

    @allure.story('Получение продуктов по категории')
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_products_by_category(self, api_client):
        response = api_client.get('/products/category/jewelery')
        assert response.status_code == 200

        products = response.json()
        assert isinstance(products, list)
        assert len(products) > 0
        for product in products:
            assert product['category'] == 'jewelery'
