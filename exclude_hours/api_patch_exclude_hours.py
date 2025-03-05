import uuid

from base import BASE_URL, API_KEY
from custom_logger import logger
from exclude_hours.api_create_exclude_hours import ExcludedHoursProfile, ExcludeHours
from exclude_hours.interfaces import Body, Api
from utils.exclude_hours_exception import ExcludeHoursException
from utils.http_client import RequestClientFactory


class ApiPatchExcludeHours(Api):


    def __init__(self, body_: Body, api_key: str, exclude_hours_id: str):
        self.data = body_.body()
        self.headers = {
            "X-Auth": api_key
        }
        self.url = f"{BASE_URL}excluded_hours_profiles/{exclude_hours_id}"

        print(self.data, 'fsdkkfsdksdfk', self.url)

        self.http_client = RequestClientFactory() \
            .create_new_client("PATCH", url=self.url,
                               json=self.data, headers=self.headers)

    def do(self):
        try:
            return self.http_client.send_request()
        except Exception as e:
            logger.error("Cannot do this request %s", str(e))
            raise ValueError(ExcludeHoursException.BAD_REQUEST)


body = ExcludedHoursProfile(
    name="test2dsaadsdsa",
)
api_create = ApiPatchExcludeHours(body, API_KEY, "8110dffb-48de-4606-8da7-68f58b7d0ea5")
api_create.do()