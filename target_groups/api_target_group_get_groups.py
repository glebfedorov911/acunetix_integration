from .api_target_group_mixin import ApiTargetGroupMixin


class ApiTargetGroupGetGroups(ApiTargetGroupMixin):


    def __init__(self, api_key: str):
        super().__init__("GET", api_key)