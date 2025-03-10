from base import BASE_URL
from .api_target_mixin import ApiTargetMixin
from .utils import TargetIdList


class ApiTargetRemoveTargets(ApiTargetMixin):
    def __init__(self, api_key: str, target: TargetIdList):
        super().__init__("POST", api_key, json=target.model_dump())
        self.url = f"{BASE_URL}/targets/delete"