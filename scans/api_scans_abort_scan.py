from base import BASE_URL
from .api_scans_mixin import ApiScanMixin
from .utils import Scan


class ApiScanAbortScan(ApiScanMixin):
    def __init__(self, api_key: str, scan_id: str):
        super().__init__("POST", api_key)
        self.url = f"{BASE_URL}/scans/{scan_id}/abort"