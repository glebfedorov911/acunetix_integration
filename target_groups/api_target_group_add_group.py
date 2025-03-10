from .api_target_group_mixin import ApiTargetGroupMixin
from .utils import TargetGroup


class ApiTargetAddGroup(ApiTargetGroupMixin):


    def __init__(self, api_key: str, target_group: TargetGroup):
        super().__init__("POST", api_key, json=target_group.model_dump())