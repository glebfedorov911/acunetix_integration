from base import BASE_URL
from custom_logger import logger
from exclude_hours.interfaces import Api
from utils.exclude_hours_exception import ExcludeHoursException
from utils.http_client import RequestClientFactory


class ApiExcludeHoursMixin(Api):


    def __init__(
            self,
            method: str,
            api_key: str,
            /,
            exclude_hours_id: str | None = None,
            json: dict | None = None
    ):
        self.url = f"{BASE_URL}/excluded_hours_profiles"
        if exclude_hours_id:
            self.url += f"/{exclude_hours_id}"

        self.headers = {
            "X-Auth": api_key
        }

        factory = RequestClientFactory()
        if not json:
            self.http_client = factory.create_new_client(
                method, url=self.url, headers=self.headers
            )
        else:
            self.http_client = factory.create_new_client(
                method, url=self.url, headers=self.headers,
                json=json
            )

    def do(self):
        try:
            return self.http_client.send_request()
        except Exception as e:
            logger.error("Cannot do this request %s", str(e))
            raise ValueError(ExcludeHoursException.BAD_REQUEST)