from base import BASE_URL
from .api_target_mixin import ApiTargetMixin
from .utils import TargetConfiguration


class ApiTargetConfigureTarget(ApiTargetMixin):
    def __init__(self, api_key: str, target_id: str, target_configuration: TargetConfiguration):
        super().__init__("PATCH", api_key, json=target_configuration.model_dump())
        self.url = f"{BASE_URL}/targets/{target_id}/configuration"