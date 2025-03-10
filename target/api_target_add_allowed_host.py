from base import BASE_URL
from .api_target_mixin import ApiTargetMixin
from .utils import TargetIdContainer


class ApiTargetAddAllowedHosts(ApiTargetMixin):
    def __init__(self, api_key: str, target_id: str, target_id_container: TargetIdContainer):
        super().__init__("POST", api_key)
        self.url = f"{BASE_URL}/targets/{target_id}/allowed_hosts"