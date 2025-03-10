from base import BASE_URL
from .api_target_mixin import ApiTargetMixin
from .utils import ContinuousScanMode


class ApiTargetSetContinuousScanStatus(ApiTargetMixin):
    def __init__(self, api_key: str, target_id: str, continuous_scan_mode: ContinuousScanMode):
        super().__init__("POST", api_key, json=continuous_scan_mode.model_dump())
        self.url = f"{BASE_URL}/targets/{target_id}/continuous_scan"