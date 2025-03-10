import uuid

from pydantic import BaseModel


class ScanningProfile(BaseModel):
    name: str | None = None
    profile_id: uuid.UUID | None = None
    sort_order: int | None = None
    custom: bool | None = None
    checks: list[str]