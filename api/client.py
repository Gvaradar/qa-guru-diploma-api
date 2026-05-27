import requests
import allure
from utils.logger import attach_request, attach_response


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        attach_request('GET', url)
        response = self.session.get(url, **kwargs)
        attach_response(response.status_code, response.json())
        return response

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        attach_request('POST', url, kwargs.get('json'))
        response = self.session.post(url, **kwargs)
        attach_response(response.status_code, response.json())
        return response

    def put(self, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        attach_request('PUT', url, kwargs.get('json'))
        response = self.session.put(url, **kwargs)
        attach_response(response.status_code, response.json())
        return response

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        attach_request('DELETE', url)
        response = self.session.delete(url, **kwargs)
        attach_response(response.status_code, response.json())
        return response