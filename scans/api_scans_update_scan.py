from base import BASE_URL
from .api_scans_mixin import ApiScanMixin
from .utils import Scan


class ApiScanUpdateScan(ApiScanMixin):
    def __init__(self, api_key: str, scan_id: str, scan: Scan):
        super().__init__("PATCH", api_key, json=scan.model_dump())
        self.url = f"{BASE_URL}/scans/{scan_id}"