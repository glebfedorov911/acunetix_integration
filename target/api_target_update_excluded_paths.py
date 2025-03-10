from base import BASE_URL
from .api_target_mixin import ApiTargetMixin
from .utils import ExcludedPathListUpdate


class ApiTargetUpdateExcludedPaths(ApiTargetMixin):
    def __init__(self, api_key: str, target_id: str, excluded_path_list_updated: ExcludedPathListUpdate):
        super().__init__("POST", api_key, json=excluded_path_list_updated.model_dump())
        self.url = f"{BASE_URL}/targets/{target_id}/configuration/exclusions"