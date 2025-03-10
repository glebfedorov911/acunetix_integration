from pydantic import BaseModel

from base import BASE_URL, API_KEY
from reports.api_reports_mixin import ApiReportsMixin


class ApiRemoveReportById(ApiReportsMixin):
    def __init__(self, api_key: str, report_id: str):
        super().__init__("DELETE", api_key)
        self.url = f"{BASE_URL}/reports/{report_id}"
