from base import BASE_URL, API_KEY
from reports.api_reports_mixin import ApiReportsMixin


class ApiDownloadReport(ApiReportsMixin):
    def __init__(self, api_key: str, descriptor: str):
        super().__init__("GET", api_key)
        self.url = f"{BASE_URL}/reports/download/{descriptor}"