import allure
import requests


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def _log_request(self, method: str, url: str, body: dict = None):
        with allure.step(f"{method} {url}"):
            if body:
                allure.attach(str(body), name="Request Body", attachment_type=allure.attachment_type.JSON)

    def _log_response(self, response):
        allure.attach(str(response.status_code), name="Response Status Code",
                      attachment_type=allure.attachment_type.TEXT)
        try:
            if response.text:
                allure.attach(response.json(), name="Response Body", attachment_type=allure.attachment_type.JSON)
            else:
                allure.attach("Empty response", name="Response Body", attachment_type=allure.attachment_type.TEXT)
        except:
            allure.attach(response.text, name="Response Body (raw)", attachment_type=allure.attachment_type.TEXT)
        return response

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        self._log_request('GET', url)
        response = self.session.get(url, **kwargs)
        return self._log_response(response)

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        self._log_request('POST', url, kwargs.get('json'))
        response = self.session.post(url, **kwargs)
        return self._log_response(response)

    def put(self, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        self._log_request('PUT', url, kwargs.get('json'))
        response = self.session.put(url, **kwargs)
        return self._log_response(response)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        self._log_request('DELETE', url)
        response = self.session.delete(url, **kwargs)
        return self._log_response(response)
