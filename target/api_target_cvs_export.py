from base import BASE_URL
from .api_target_mixin import ApiTargetMixin


class ApiTargetCSVExport(ApiTargetMixin):
    def __init__(self, api_key: str):
        super().__init__("GET", api_key)
        self.url = f"{BASE_URL}/targets/cvs_export"