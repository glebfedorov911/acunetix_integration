from base import BASE_URL
from .api_scanning_profiles_mixin import ApiScanningProfilesMixin


class ApiScanningProfilesGetScanningProfiles(ApiScanningProfilesMixin):
    def __init__(self, api_key: str):
        super().__init__("GET", api_key)