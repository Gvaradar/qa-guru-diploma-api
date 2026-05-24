import allure
from jsonschema import validate
from api.client import ApiClient
from api.schemas import product_schema, products_list_schema


@allure.epic('API тестирование')
@allure.feature('Products API')
class TestProductsAPI:

    @allure.story('GET запросы')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_all_products(self, api_client):
        response = api_client.get('/products')

        assert response.status_code == 200
        products = response.json()
        assert isinstance(products, list)
        assert len(products) > 0
        validate(instance=products, schema=products_list_schema)

    @allure.story('GET запросы')
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_single_product(self, api_client):
        response = api_client.get('/products/1')

        assert response.status_code == 200
        product = response.json()
        assert product['id'] == 1
        assert product['title'] == 'Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops'
        validate(instance=product, schema=product_schema)

    @allure.story('POST запросы')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_product(self, api_client):
        new_product = {
            "title": "Test Product",
            "price": 99.99,
            "description": "Test description",
            "category": "electronic",
            "image": "https://via.placeholder.com/300"
        }

        response = api_client.post('/products', json=new_product)

        assert response.status_code == 201
        created = response.json()
        assert created['title'] == new_product['title']
        assert created['price'] == new_product['price']
        assert 'id' in created

    @allure.story('DELETE запросы')
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_product(self, api_client):
        response = api_client.delete('/products/1')

        assert response.status_code == 200
        assert response.json()['id'] == 1

    @allure.story('PUT запросы')
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

        assert response.status_code == 200
        result = response.json()
        assert result['title'] == "Updated Backpack"
        assert result['price'] == 129.95