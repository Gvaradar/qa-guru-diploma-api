import requests
import allure
from utils.logger import attach_request, attach_response


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    def _log_response(self, response):
        allure.attach(str(response.status_code), name="Response Status Code", attachment_type=allure.attachment_type.TEXT)
        try:
            allure.attach(response.json(), name="Response Body", attachment_type=allure.attachment_type.JSON)
        except:
            allure.attach(response.text, name="Response Body (raw)", attachment_type=allure.attachment_type.TEXT)

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        attach_request('GET', url)
        response = self.session.get(url, **kwargs)
        self._log_response(response)
        return response

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        attach_request('POST', url, kwargs.get('json'))
        response = self.session.post(url, **kwargs)
        self._log_response(response)
        return response

    def put(self, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        attach_request('PUT', url, kwargs.get('json'))
        response = self.session.put(url, **kwargs)
        self._log_response(response)
        return response

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        attach_request('DELETE', url)
        response = self.session.delete(url, **kwargs)
        self._log_response(response)
        return response