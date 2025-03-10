from base import API_KEY
from exclude_hours.api_delete_exclude_hours import ApiDeleteExcludeHours


delete = ApiDeleteExcludeHours(
    API_KEY,
    "2c17f6dd-7e3c-44fa-bb95-b269f65d1dbd"
)
delete.do()