from another.export_group_scan import BASE_URL
from .api_target_group_mixin import ApiTargetGroupMixin
from .utils import TargetGroup


class ApiTargetChangeGroup(ApiTargetGroupMixin):


    def __init__(self, api_key: str, group_id: str, target_group: TargetGroup):
        super().__init__("PATCH", api_key, json=target_group.model_dump())
        self.url = f"{BASE_URL}/target_groups/{group_id}"