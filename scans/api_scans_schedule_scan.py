from base import BASE_URL
from .api_scans_mixin import ApiScanMixin
from .utils import Scan


class ApiScanScheduleScan(ApiScanMixin):
    def __init__(self, api_key: str, scan: Scan):
        super().__init__("POST", api_key, json=scan.model_dump())