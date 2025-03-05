from base import BASE_URL, API_KEY
from custom_logger import logger
from exclude_hours.interfaces import Api
from utils.exclude_hours_exception import ExcludeHoursException
from utils.http_client import RequestClientFactory


class ApiGetByIDExcludeHours(Api):


    def __init__(self, exclude_hours_id: str):
        self.url = f"{BASE_URL}excluded_hours_profiles/{exclude_hours_id}"
        self.headers = {
            "X-Auth": API_KEY
        }

        self.http_client = RequestClientFactory().create_new_client("GET", url=self.url, headers=self.headers)

    def do(self):
        try:
            return self.http_client.send_request()
        except Exception as e:
            logger.error("Cannot do this request %s", str(e))
            raise ValueError(ExcludeHoursException.BAD_REQUEST)

api = ApiGetByIDExcludeHours("8110dffb-48de-4606-8da7-68f58b7d0ea5")
print(api.do())