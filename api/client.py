import requests
import allure
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    def _log_request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"REQUEST: {method} {url}")
        if 'json' in kwargs:
            logger.info(f"BODY: {kwargs['json']}")

        with allure.step(f"{method} {endpoint}"):
            allure.attach(str(kwargs.get('json', {})), name='Request Body', attachment_type=allure.attachment_type.JSON)

    def _log_response(self, response, endpoint: str):
        logger.info(f"RESPONSE: {response.status_code} - {self.base_url}{endpoint}")
        logger.info(f"BODY: {response.text[:200]}")
        allure.attach(str(response.status_code), name='Response Status Code', attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name='Response Body', attachment_type=allure.attachment_type.JSON)

    def get(self, endpoint: str, **kwargs):
        self._log_request('GET', endpoint, **kwargs)
        response = self.session.get(f"{self.base_url}{endpoint}", **kwargs)
        self._log_response(response, endpoint)
        return response

    def post(self, endpoint: str, **kwargs):
        self._log_request('POST', endpoint, **kwargs)
        response = self.session.post(f"{self.base_url}{endpoint}", **kwargs)
        self._log_response(response, endpoint)
        return response

    def put(self, endpoint: str, **kwargs):
        self._log_request('PUT', endpoint, **kwargs)
        response = self.session.put(f"{self.base_url}{endpoint}", **kwargs)
        self._log_response(response, endpoint)
        return response

    def delete(self, endpoint: str, **kwargs):
        self._log_request('DELETE', endpoint, **kwargs)
        response = self.session.delete(f"{self.base_url}{endpoint}", **kwargs)
        self._log_response(response, endpoint)
        return response