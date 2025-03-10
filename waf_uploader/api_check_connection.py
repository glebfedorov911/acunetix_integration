from base import BASE_URL
from .api_waf_uploader_mixin import ApiWafUploaderMixin
from .utils import WAFConfig


class ApiWafCheckConnection(ApiWafUploaderMixin):
    def __init__(self, api_key: str, waf_config: WAFConfig):
        super().__init__("POST", api_key, json=waf_config.model_dump())
        self.url = f"{BASE_URL}/wafs/check_connection"