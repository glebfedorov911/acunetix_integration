from base import BASE_URL
from .api_waf_uploader_mixin import ApiWafUploaderMixin


class ApiWafGetEntry(ApiWafUploaderMixin):
    def __init__(self, api_key: str, waf_id: str):
        super().__init__("GET", api_key)
        self.url = f"{BASE_URL}/wafs/{waf_id}"