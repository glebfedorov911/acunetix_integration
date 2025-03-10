from base import BASE_URL, API_KEY
from reports.api_reports_mixin import ApiReportsMixin


class ApiRepeatReport(ApiReportsMixin):
    def __init__(self, api_key: str, report_id: str):
        super().__init__("POST", api_key)
        self.url = f"{BASE_URL}/reports/{report_id}/repeat"