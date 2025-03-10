from base import BASE_URL
from .api_worker_manager_mixin import ApiWorkerManagerMixin


class ApiWorkerManagerGetWorkers(ApiWorkerManagerMixin):
    def __init__(self, api_key: str):
        super().__init__("GET", api_key)
        self.url = f"{BASE_URL}/workers"