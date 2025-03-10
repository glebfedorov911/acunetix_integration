from exclude_hours.api_exclude_hours_mixin import ApiExcludeHoursMixin


class ApiDeleteExcludeHours(ApiExcludeHoursMixin):


    def __init__(
            self,
            api_key: str,
            exclude_hours_id: str
    ):
        super().__init__(
            "DELETE", api_key,
            exclude_hours_id=exclude_hours_id,
        )