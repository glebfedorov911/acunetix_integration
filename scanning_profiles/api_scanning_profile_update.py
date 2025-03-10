from base import BASE_URL
from .api_scanning_profiles_mixin import ApiScanningProfilesMixin
from .utils import ScanningProfile


class ApiScanningProfilesUpdateScanningProfile(ApiScanningProfilesMixin):
    def __init__(self, api_key: str, scanning_profile_id: str, scanning_profile: ScanningProfile):
        super().__init__("PATCH", api_key, json=scanning_profile.model_dump())
        self.url = f"{BASE_URL}/scanning_profiles/{scanning_profile_id}"