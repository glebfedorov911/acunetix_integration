from .api_target_mixin import ApiTargetMixin
from .utils import Target


class ApiTargetAddTarget(ApiTargetMixin):
    def __init__(self, api_key: str, target: Target):
        super().__init__("POST", api_key, json=target.model_dump())