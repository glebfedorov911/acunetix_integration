from pydantic import BaseModel


class SeverityCounts(BaseModel):
    critical: int | None = None
    high: int | None = None
    medium: int | None = None
    low: int | None = None
    info: int | None = None

class TargetGroup(BaseModel):
    group_id: str | None = None
    name: str
    target_count: int | None = None
    description: str | None = None
    vuln_count:  SeverityCounts | None = None

class TargetGroupIdList(BaseModel):
    group_id_list: list[str] | None = []

class GroupChangeTargetIdList(BaseModel):
    remove: list[str] | None = []
    add: list[str] | None = []

class TargetIdList(BaseModel):
    target_id_list: list[str] | None = []