from base import BASE_URL
from .api_worker_manager_mixin import ApiWorkerManagerMixin


class ApiWorkerManagerDeleteWorker(ApiWorkerManagerMixin):
    def __init__(self, api_key: str, worker_id: str):
        super().__init__("DELETE", api_key)
        self.url = f"{BASE_URL}/workers/{worker_id}"