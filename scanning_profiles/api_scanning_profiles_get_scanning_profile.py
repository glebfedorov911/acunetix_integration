from base import BASE_URL
from .api_scanning_profiles_mixin import ApiScanningProfilesMixin


class ApiScanningProfilesGetScanningProfile(ApiScanningProfilesMixin):
    def __init__(self, api_key: str, scanning_profile_id: str):
        super().__init__("GET", api_key)
        self.url = f"{BASE_URL}/scanning_profiles/{scanning_profile_id}"