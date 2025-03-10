from .api_scanning_profiles_mixin import ApiScanningProfilesMixin
from .utils import ScanningProfile


class ApiScanningProfilesCreateScanningProfile(ApiScanningProfilesMixin):
    def __init__(self, api_key: str, scanning_profile: ScanningProfile):
        super().__init__("POST", api_key, json=scanning_profile.model_dump())