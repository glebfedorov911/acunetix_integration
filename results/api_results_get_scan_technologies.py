from base import BASE_URL
from .api_results_mixin import ApiResultsMixin


class ApiGetScanTechnologiesResult(ApiResultsMixin):
    def __init__(self, api_key: str, /,
                 scan_id: str, result_id: str):
        super().__init__("GET", api_key)
        self.url = f"{BASE_URL}/scans/{scan_id}/results/{result_id}/technologies"