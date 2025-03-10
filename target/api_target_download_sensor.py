from base import BASE_URL
from .api_target_mixin import ApiTargetMixin


class ApiTargetDownloadSensor(ApiTargetMixin):
    def __init__(self, api_key: str, sensor_type: str, sensor_secret: str):
        super().__init__("GET", api_key)
        self.url = f"{BASE_URL}/targets/sensors/{sensor_type}/{sensor_secret}"