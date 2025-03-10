from base import BASE_URL
from .api_target_group_mixin import ApiTargetGroupMixin


class ApiTargetListTargets(ApiTargetGroupMixin):


    def __init__(self, api_key: str, group_id: str):
        super().__init__("GET", api_key)
        self.url = f"{BASE_URL}/target_groups/{group_id}/targets"