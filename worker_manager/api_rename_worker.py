from base import BASE_URL
from .api_worker_manager_mixin import ApiWorkerManagerMixin
from .utils import WorkerDescription


class ApiWorkerManagerRenameWorker(ApiWorkerManagerMixin):
    def __init__(self, api_key: str, worker_id: str, worker_description: WorkerDescription):
        super().__init__("POST", api_key, json=worker_description.model_dump())
        self.url = f"{BASE_URL}/workers/{worker_id}/rename"