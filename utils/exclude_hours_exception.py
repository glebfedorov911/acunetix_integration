from enum import Enum


class ExcludeHoursException(Enum):
    NOT_VALID_DAY_OF_WEEK = "Not valid day of week. Need from 1 to 7"
    NOT_VALID_TIME = "Not valid time. Need from 0 to 23"
    BAD_REQUEST = "Bad request"