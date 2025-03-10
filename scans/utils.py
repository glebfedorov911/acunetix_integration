from datetime import datetime

from pydantic import BaseModel


class Schedule(BaseModel):
    disable: bool | None = None
    time_sensitive: bool | None = None
    history_limit: int | None = None
    start_date: datetime | None = None
    recurrence: str | None = None
    triggerable: bool | None = None

class Scan(BaseModel):
    target_id: str
    profile_id: str
    report_template_id: str | None = None
    schedule: Schedule
    max_scan_time: int | None = None
    incremental: bool | None = None
    next_run: datetime | None = None