from pydantic import BaseModel


class EmptyObject(BaseModel): ...

class WorkerDescription(BaseModel):
    description: str | None = None

class WorkerIdList(BaseModel):
    worker_id_list: list[str] | None = []