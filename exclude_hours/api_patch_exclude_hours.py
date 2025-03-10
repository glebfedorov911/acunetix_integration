from exclude_hours.api_exclude_hours_mixin import ApiExcludeHoursMixin
from exclude_hours.interfaces import Body


class ApiPatchExcludeHours(ApiExcludeHoursMixin):


    def __init__(
            self,
            body_: Body,
            api_key: str,
            exclude_hours_id: str
    ):
        super().__init__(
            "PATCH", api_key,
             exclude_hours_id=exclude_hours_id,
             json=body_.body()
         )