from base import BASE_URL
from .api_target_group_mixin import ApiTargetGroupMixin
from .utils import GroupChangeTargetIdList


class ApiTargetChangeTargets(ApiTargetGroupMixin):


    def __init__(self, api_key: str, group_id: str, group_change_target_id_list: GroupChangeTargetIdList):
        super().__init__("PATCH", api_key, json=group_change_target_id_list.model_dump())
        self.url = f"{BASE_URL}/target_groups/{group_id}/targets"