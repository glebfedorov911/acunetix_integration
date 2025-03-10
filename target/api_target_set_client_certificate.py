from base import BASE_URL
from .api_target_mixin import ApiTargetMixin
from .utils import FileUploadDescriptor


class ApiTargetSetClientCertificate(ApiTargetMixin):
    def __init__(self, api_key: str, target_id: str, file_upload_request: FileUploadDescriptor):
        super().__init__("POST", api_key, json=file_upload_request.model_dump())
        self.url = f"{BASE_URL}/targets/{target_id}/configuration/client_certificate"