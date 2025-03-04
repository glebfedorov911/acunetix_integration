from abc import ABC, abstractmethod

from base import TARGET_API_URL
from utils.http_client import GetHttpRequestClient, PostHttpRequestClient, HttpClient
from custom_logger import logger


class TargetHandler(ABC):

    @abstractmethod
    def run(self) -> dict:
        ...

class BaseTargetHandler(TargetHandler):


    def __init__(self, url: str, http_client: HttpClient, **kwargs):
        self.url = url
        self.http_client = http_client

    def run(self) -> dict:
        ...

class TargetGetHandler(BaseTargetHandler):


    def __init__(self, http_client: GetHttpRequestClient):
        super().__init__(TARGET_API_URL, http_client)

    def run(self) -> dict:
        try:
            targets = self._get_targets()
            logger.info("Got %s targets", len(targets))
            return targets
        except Exception as e:
            logger.exception(e)
            raise Exception("Failed to get targets")

    def _get_targets(self) -> dict:
        logger.info("Getting targets from %s", self.url)
        return self.http_client.send_request()

class TargetAddHandler(BaseTargetHandler):


    def __init__(self, http_client: PostHttpRequestClient):
        super().__init__(TARGET_API_URL, http_client)

    def run(self) -> dict:
        try:
            new_target = self._add_target()
            logger.info("Success added new target")
            return new_target
        except Exception as e:
            logger.exception(e)
            raise Exception("Failed to get targets")

    def _add_target(self):
        logger.info("Create new target from %s", self.url)
        return self.http_client.send_request()