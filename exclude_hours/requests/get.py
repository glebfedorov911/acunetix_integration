from base import API_KEY
from exclude_hours.api_get_by_id_exclude_hours import ApiGetByIDExcludeHours
from exclude_hours.api_get_exclude_hours import ApiGetExcludeHours


get = ApiGetExcludeHours(
    API_KEY
)
get.do()

# get_id = ApiGetByIDExcludeHours(
#     API_KEY,
#     "2c17f6dd-7e3c-44fa-bb95-b269f65d1dbd"
# )
# get_id.do()