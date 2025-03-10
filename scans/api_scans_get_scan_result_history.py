from base import BASE_URL
from .api_scans_mixin import ApiScanMixin


class ApiScanGetScanResultHistory(ApiScanMixin):
    def __init__(self, api_key: str, scan_id: str):
        super().__init__("GET", api_key)
        self.url = f"{BASE_URL}/scans/{scan_id}/results"