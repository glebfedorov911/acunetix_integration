from base import BASE_URL
from custom_logger import logger
from utils.http_client import RequestClientFactory
from utils.interfaces import Api


class ApiGetReportTemplates(Api):
    def __init__(self, method: str, api_key: str):
        self.url = f"{BASE_URL}/report_templates"
        self.headers = {
            "X-Auth": api_key
        }

        self.http_client = RequestClientFactory().create_new_client(
            method, url=self.url, headers=self.headers
        )

    def do(self):
        try:
            return self.http_client.send_request()
        except Exception as e:
            logger.error("Cannot do this request %s", str(e))
            raise ValueError(str(e))