from base import BASE_URL
from .api_target_mixin import ApiTargetMixin
from .utils import SensorSecretContainer


class ApiTargetResetSensorSecret(ApiTargetMixin):
    def __init__(self, api_key: str, target_id: str, sensor_secret_container: SensorSecretContainer):
        super().__init__("POST", api_key, json=sensor_secret_container.model_dump())
        self.url = f"{BASE_URL}/targets/{target_id}/sensor/reset"