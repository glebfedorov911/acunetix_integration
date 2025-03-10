from exclude_hours.api_exclude_hours_mixin import ApiExcludeHoursMixin


class ApiGetExcludeHours(ApiExcludeHoursMixin):


    def __init__(
            self,
            api_key: str,
    ):
        super().__init__("GET", api_key)