from base import BASE_URL
from .api_target_group_mixin import ApiTargetGroupMixin
from .utils import TargetIdList


class ApiTargetSetTargets(ApiTargetGroupMixin):


    def __init__(self, api_key: str, group_id: str, target_id_list: TargetIdList):
        super().__init__("POST", api_key, json=target_id_list.model_dump())
        self.url = f"{BASE_URL}/target_groups/{group_id}/targets"