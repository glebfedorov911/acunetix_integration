import uuid
from typing import List

from pydantic import BaseModel, field_validator, model_validator

from exclude_hours.interfaces import Body
from utils.exclude_hours_exception import ExcludeHoursException


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
        if not (1 <= self.start_time <= self.finish_time <= 24):
            raise ValueError(ExcludeHoursException.NOT_VALID_TIME)
        return self


class ExcludedHoursProfileMixin(Body):
    def __init__(
            self,
            name: str,
            exclude_hours_id: uuid.UUID,
            time_offset: int,
            exclude_hours: List[ExcludeHours]
    ):
        self.name = name
        self.exclude_hours_id = exclude_hours_id
        self.time_offset = time_offset #Смещение по часовому поясу в минутах
        self.exclude_hours = exclude_hours

        self.hours_in_week = 168
        self.hour_in_day = 24

    def body(self):
        result = {
            "name": self.name,
            "excluded_hours_id": str(self.exclude_hours_id),
            "time_offset": self.time_offset,
            "exclusion_matrix": ExcludeHoursConverter(self.exclude_hours).to_matrix()
        }
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

class ExcludedHoursProfileCreate(ExcludedHoursProfileMixin):
    def __init__(
            self,
            name: str,
            exclude_hours_id: uuid.UUID,
            exclude_hours: List[ExcludeHours],
            time_offset: int = 0,
    ):
        super().__init__(name, exclude_hours_id, time_offset, exclude_hours)

class ExcludedHoursProfileUpdate(ExcludedHoursProfileMixin):
    def __init__(
            self,
            name: str,
            exclude_hours_id: uuid.UUID,
            time_offset: int,
            exclude_hours: List[ExcludeHours]
    ):
        super().__init__(name, exclude_hours_id, time_offset, exclude_hours)