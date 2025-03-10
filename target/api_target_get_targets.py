from .api_target_mixin import ApiTargetMixin


class ApiTargetGetTargets(ApiTargetMixin):
    def __init__(self, api_key: str):
        super().__init__("GET", api_key)