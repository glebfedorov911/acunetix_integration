from base import BASE_URL
from reports.api_reports_mixin import ApiReportsMixin


class ApiGetReportTemplates(ApiReportsMixin):
    def __init__(self, api_key: str):
        super().__init__("GET", api_key)
        self.url = f"{BASE_URL}/report_templates"