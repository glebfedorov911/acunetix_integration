from abc import ABC, abstractmethod
import requests

from custom_logger import logger


class HttpClient(ABC):


    @abstractmethod
    def send_request(self) -> dict:
        ...

class HttpRequestClient(HttpClient):


    def __init__(self, url: str, method: str, **kwargs):
        self.url = url
        self.method = method
        self.kwargs = kwargs

    def send_request(self) -> dict:
        try:
            logger.info("Sending %s request to %s", self.method, self.url)
            return self._send_request()
        except requests.exceptions.Timeout as e:
            logger.exception(e)
            raise Exception("Timeout error")
        except requests.exceptions.RequestException as e:
            logger.exception(e)
            raise Exception("Failed to send request")
        except Exception as e:
            logger.exception(e)
            raise e

    def _send_request(self) -> dict:
        response = requests.request(self.method, self.url, **self.kwargs)
        response.raise_for_status()

        logger.info("Success send request to %s", self.url)
        return response.json()

class GetHttpRequestClient(HttpRequestClient):


    def __init__(self, url: str, **kwargs):
        super().__init__(url, "GET", **kwargs)

class PostHttpRequestClient(HttpRequestClient):


    def __init__(self, url: str, **kwargs):
        super().__init__(url, "POST", **kwargs)