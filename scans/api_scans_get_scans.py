from base import BASE_URL
from .api_scans_mixin import ApiScanMixin


class ApiScanGetScans(ApiScanMixin):
    def __init__(self, api_key: str):
        super().__init__("GET", api_key)