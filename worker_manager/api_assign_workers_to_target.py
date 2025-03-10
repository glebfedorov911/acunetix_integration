from base import BASE_URL
from .api_worker_manager_mixin import ApiWorkerManagerMixin
from .utils import WorkerIdList


class ApiWorkerManagerAssignedToTarget(ApiWorkerManagerMixin):
    def __init__(self, api_key: str, target_id: str, worker_id_list: WorkerIdList):
        super().__init__("POST", api_key, json=worker_id_list.model_dump())
        self.url = f"{BASE_URL}/targets/{target_id}/configuration/workers"