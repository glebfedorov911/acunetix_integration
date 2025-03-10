from base import BASE_URL
from .api_target_group_mixin import ApiTargetGroupMixin
from .utils import TargetGroupIdList


class ApiTargetDeleteGroup(ApiTargetGroupMixin):


    def __init__(self, api_key: str, target_group_id_list: TargetGroupIdList):
        super().__init__("POST", api_key, json=target_group_id_list.model_dump())
        self.url = f"{BASE_URL}/target_groups/delete"