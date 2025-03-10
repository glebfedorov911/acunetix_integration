from base import BASE_URL
from .api_worker_manager_mixin import ApiWorkerManagerMixin
from .utils import EmptyObject


class ApiWorkerManagerRejectWorker(ApiWorkerManagerMixin):
    def __init__(self, api_key: str, worker_id: str, empty_object: EmptyObject):
        super().__init__("POST", api_key, json=empty_object.model_dump())
        self.url = f"{BASE_URL}/workers/{worker_id}/reject"