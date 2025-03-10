from base import BASE_URL
from .api_target_mixin import ApiTargetMixin


class ApiTargetDeleteImportedFile(ApiTargetMixin):
    def __init__(self, api_key: str, target_id: str, import_id: str):
        super().__init__("DELETE", api_key)
        self.url = f"{BASE_URL}/targets/{target_id}/configuration/imports/{import_id}"