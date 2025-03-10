from base import BASE_URL
from custom_logger import logger
from utils.http_client import RequestClientFactory
from utils.http_client_exception import HttpClientException
from utils.http_error_handler import HttpError
from utils.interfaces import Api


class ApiResultsMixin(Api):
    def __init__(
            self,
            method: str,
            api_key: str,
            /,
            json: dict | None = None
    ):
        self.url = f"{BASE_URL}/results"
        self.headers = {
            "X-Auth": api_key
        }

        if json:
            self.http_client = RequestClientFactory().create_new_client(
                method, url=self.url, headers=self.headers, json=json
            )
        else:
            self.http_client = RequestClientFactory().create_new_client(
                method, url=self.url, headers=self.headers
            )

    def do(self):
        try:
            return self.http_client.send_request()
        except HttpError as e:
            logger.error("Cannot do this request %s", str(e))
            raise ValueError(str(e))
        except Exception as e:
            logger.error("Cannot do this request %s", str(e))
            raise ValueError(HttpClientException.ERROR_SEND_REQUEST.value)