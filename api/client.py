import requests
from utils.logger import attach_request, attach_response


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def _log_response(self, response):
        attach_response(response.status_code, response.text)
        return response

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        attach_request('GET', url)
        response = self.session.get(url, **kwargs)
        return self._log_response(response)

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        attach_request('POST', url, kwargs.get('json'))
        response = self.session.post(url, **kwargs)
        return self._log_response(response)

    def put(self, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        attach_request('PUT', url, kwargs.get('json'))
        response = self.session.put(url, **kwargs)
        return self._log_response(response)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        attach_request('DELETE', url)
        response = self.session.delete(url, **kwargs)
        return self._log_response(response)