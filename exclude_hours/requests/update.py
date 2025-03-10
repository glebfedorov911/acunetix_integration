import uuid

from base import API_KEY
from exclude_hours.api_patch_exclude_hours import ApiPatchExcludeHours
from exclude_hours.utils import ExcludedHoursProfileUpdate, ExcludeHours


body = ExcludedHoursProfileUpdate(
    name="Even day of week",
    exclude_hours_id=uuid.UUID("2c17f6dd-7e3c-44fa-bb95-b269f65d1dbd"),
    time_offset=180,
    exclude_hours=[
        ExcludeHours(
            day_of_week=1,
            start_time=1,
            finish_time=24
        ),
        ExcludeHours(
            day_of_week=3,
            start_time=1,
            finish_time=24,
        ),
        ExcludeHours(
            day_of_week=5,
            start_time=1,
            finish_time=24,
        ),
        ExcludeHours(
            day_of_week=7,
            start_time=1,
            finish_time=24,
        )
    ]
)

exclude_hours_id = "2c17f6dd-7e3c-44fa-bb95-b269f65d1dbd"
patch = ApiPatchExcludeHours(
    body,
    API_KEY,
    exclude_hours_id
)
patch.do()