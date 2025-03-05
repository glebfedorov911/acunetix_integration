from abc import ABC, abstractmethod

import requests
import urllib3

from custom_logger import logger
from utils.http_client_exception import (
    FactoryHttpClientException, HttpClientException
)


urllib3.disable_warnings()

class HttpClient(ABC):


    @abstractmethod
    def send_request(self): ...

class HttpRequestClient(HttpClient):


    def __init__(
            self,
            url: str,
            method: str,
            /,
            json: dict | None = None,
            headers: dict | None = None,
            proxy: dict | None = None
    ):
        self.url = url
        self.method = method
        self.json = json
        self.headers = headers
        self.proxy = proxy

    def send_request(self) -> dict:
        try:
            return self._send_request()
        except requests.exceptions.RequestException as e:
            logger.error("Error sending request to %s: %s", self.url, str(e))
            raise ValueError(HttpClientException.ERROR_SEND_REQUEST)

    def _send_request(self) -> dict:
        logger.info("Sending %s request to %s", self.method, self.url)
        response = requests.request(self.method, self.url, json=self.json,
                                   headers=self.headers, proxies=self.proxy,
                                   verify=False)
        logger.info("Response %s", response.text)
        response.raise_for_status()

        logger.info("Request sent successfully to %s", self.url)
        return response.text

class GetRequestClient(HttpRequestClient):


    def __init__(self, url: str, headers: dict | None = None, proxy: dict | None = None):
        super().__init__(url, "GET", headers=headers, proxy=proxy)

class PostRequestClient(HttpRequestClient):


    def __init__(self, url: str, json: dict | None = None, headers: dict | None = None, proxy: dict | None = None):
        super().__init__(url, "POST", json=json, headers=headers, proxy=proxy)

class PutRequestClient(HttpRequestClient):


    def __init__(self, url: str, json: dict | None, headers: dict | None = None, proxy: dict | None = None):
        super().__init__(url, "PUT", json=json, headers=headers, proxy=proxy)

class PatchRequestClient(HttpRequestClient):


    def __init__(self, url: str, json: dict | None, headers: dict | None = None, proxy: dict | None = None):
        super().__init__(url, "PATCH", json=json, headers=headers, proxy=proxy)

class DeleteRequestClient(HttpRequestClient):


    def __init__(self, url: str, headers: dict | None = None, proxy: dict | None = None):
        super().__init__(url, "DELETE", headers=headers, proxy=proxy)

class RequestClientFactory:


    def create_new_client(self, method, /, **kwargs) -> HttpRequestClient:
        method = method.lower()
        if method == "get":
            return GetRequestClient(**kwargs)
        elif method == "post":
            return PostRequestClient(**kwargs)
        elif method == "put":
            return PutRequestClient(**kwargs)
        elif method == "patch":
            return PatchRequestClient(**kwargs)
        elif method == "delete":
            return DeleteRequestClient(**kwargs)
        else:
            logger.error(FactoryHttpClientException.NOT_FOUND_METHOD)
            raise ValueError(FactoryHttpClientException.NOT_FOUND_METHOD)