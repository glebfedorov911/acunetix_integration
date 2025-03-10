from base import API_KEY
from exclude_hours.api_delete_exclude_hours import ApiDeleteExcludeHours


delete = ApiDeleteExcludeHours(
    API_KEY,
    "16485d33-c0bc-49f0-92f9-d99380020b1c",
)
delete.do()