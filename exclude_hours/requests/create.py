import uuid

from base import API_KEY
from exclude_hours.api_create_exclude_hours import ApiCreateExcludeHours
from exclude_hours.utils import ExcludedHoursProfileCreate, ExcludeHours


body = ExcludedHoursProfileCreate(
    name="Even day of week",
    exclude_hours_id=uuid.uuid4(),
    time_offset=0,
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

create = ApiCreateExcludeHours(
    body,
    API_KEY
)
create.do()