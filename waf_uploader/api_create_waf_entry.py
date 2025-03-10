from base import BASE_URL
from .api_waf_uploader_mixin import ApiWafUploaderMixin
from .utils import WAFEntry


class ApiCreateWafEntry(ApiWafUploaderMixin):
    def __init__(self, api_key: str, waf_entry: WAFEntry):
        super().__init__("POST", api_key, json=waf_entry.model_dump())
        self.url = f"{BASE_URL}/wafs"