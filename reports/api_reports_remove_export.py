from base import BASE_URL, API_KEY
from reports.api_reports_mixin import ApiReportsMixin


class ApiRemoveExportByIdReports(ApiReportsMixin):
    def __init__(self, api_key: str, export_id: str):
        super().__init__("DELETE", api_key)
        self.url = f"{BASE_URL}/export_id/{export_id}"
