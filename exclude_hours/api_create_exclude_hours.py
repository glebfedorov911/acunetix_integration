from typing import List
import uuid
import json

from pydantic import BaseModel, field_validator, model_validator

from custom_logger import logger
from utils.exclude_hours_exception import ExcludeHoursException
from utils.http_client import RequestClientFactory
from .interfaces import Body, Api
from base import BASE_URL, API_KEY


class ExcludeHours(BaseModel):
    day_of_week: int
    start_time: int
    finish_time: int

    @classmethod
    @field_validator('day_of_week')
    def day_of_week_validator(cls, value):
        if not (1 <= value <= 7):
            raise ValueError(ExcludeHoursException.NOT_VALID_DAY_OF_WEEK)
        return value

    @model_validator(mode='after')
    def time_validator(self):
        if not (0 <= self.start_time <= self.finish_time <= 24):
            raise ValueError(ExcludeHoursException.NOT_VALID_TIME)
        return self


class ExcludedHoursProfile(Body):


    def __init__(
            self,
            name: str,
            exclude_hours_id: uuid.UUID | None = None,
            time_offset: int | None = None,
            exclude_hours: List[ExcludeHours] | None = None
    ):
        self.name = name
        self.exclude_hours_id = exclude_hours_id
        self.time_offset = time_offset
        self.exclude_hours = exclude_hours

        self.hours_in_week = 168
        self.hour_in_day = 24

    def body(self):
        if self.exclude_hours_id:
            self.exclude_hours_id = str(self.exclude_hours_id)

        result = {
            "name": self.name,
            "excluded_hours_id": self.exclude_hours_id,
            "time_offset": self.time_offset,
            "exclusion_matrix": ExcludeHoursConverter(self.exclude_hours).to_matrix()
        }
        return self._delete_node_fields(result)

    @staticmethod
    def _delete_node_fields(result: dict) -> dict:
        for r in list(result.keys()):
            if not result[r]:
                del result[r]

        return result

class ExcludeHoursConverter:


    HOURS_IN_WEEK = 168
    HOURS_IN_DAY = 24

    def __init__(self, exclude_hours: List[ExcludeHours]):
        self.exclude_hours = exclude_hours

    def to_matrix(self) -> List:
        matrix_exclude_hours = [False] * self.HOURS_IN_WEEK

        if not self.exclude_hours:
            return matrix_exclude_hours

        for exclude_hour in self.exclude_hours:
            day_of_week = self._get_day_of_week_decrement(exclude_hour)
            for hour in self._get_range_hours(exclude_hour):
                exclude_hour = self._get_index_hour_exclude(day_of_week, hour)
                matrix_exclude_hours[exclude_hour] = True

        return matrix_exclude_hours

    @staticmethod
    def _get_day_of_week_decrement(exclude_hour: ExcludeHours) -> int:
        return exclude_hour.day_of_week - 1

    @staticmethod
    def _get_range_hours(exclude_hour: ExcludeHours):
        return range(exclude_hour.start_time-1, exclude_hour.finish_time)

    def _get_index_hour_exclude(self, day_of_week, hour):
        return day_of_week * self.HOURS_IN_DAY + hour

class ApiCreateExcludeHours(Api):


    def __init__(self, body_: Body, api_key: str):
        self.data = body_.body()
        self.headers = {
            "X-Auth": api_key
        }
        self.url = f"{BASE_URL}excluded_hours_profiles"

        self.http_client = RequestClientFactory()\
            .create_new_client("POST", url=self.url,
            json=self.data, headers=self.headers)

    def do(self):
        try:
            return self.http_client.send_request()
        except Exception as e:
            logger.error("Cannot do this request %s", str(e))
            raise ValueError(ExcludeHoursException.BAD_REQUEST)


body = ExcludedHoursProfile(
    name="test1",
    exclude_hours_id=uuid.uuid4(),
    exclude_hours=[
        ExcludeHours(day_of_week=1, start_time=15, finish_time=20),
        ExcludeHours(day_of_week=4, start_time=5, finish_time=10),
    ]
)
# api_create = ApiCreateExcludeHours(body, API_KEY)
# api_create.do()