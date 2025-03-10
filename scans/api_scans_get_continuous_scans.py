from base import BASE_URL
from .api_scans_mixin import ApiScanMixin


class ApiScanGetContinuousScans(ApiScanMixin):
    def __init__(self, api_key: str, target_id: str):
        super().__init__("GET", api_key)
        self.url = f"{BASE_URL}/targets/{target_id}/continuous_scan/list"