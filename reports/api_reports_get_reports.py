from base import BASE_URL, API_KEY
from reports.api_reports_mixin import ApiReportsMixin


class ApiGetReports(ApiReportsMixin):
    def __init__(self, api_key: str):
        super().__init__("GET", api_key)

