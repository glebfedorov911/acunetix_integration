from .api_exclude_hours_mixin import ApiExcludeHoursMixin
from utils.interfaces import Body


class ApiCreateExcludeHours(ApiExcludeHoursMixin):


    def __init__(
            self,
            body_: Body,
            api_key: str
    ):
        super().__init__("POST", api_key, json=body_.body())

