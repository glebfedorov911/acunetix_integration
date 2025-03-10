from base import BASE_URL, API_KEY
from reports.api_reports_mixin import ApiReportsMixin


class ApiGetExportReports(ApiReportsMixin):
    def __init__(self, api_key: str, export_id: str):
        super().__init__("GET", api_key)
        self.url = f"{BASE_URL}/exports/{export_id}"