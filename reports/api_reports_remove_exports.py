from base import BASE_URL, API_KEY
from reports.api_reports_mixin import ApiReportsMixin
from reports.utils import ReportIdList


class ApiRemoveExportsReports(ApiReportsMixin):
    def __init__(self, api_key: str, report_ids: ReportIdList):
        super().__init__("POST", api_key, json=report_ids.model_dump())
        self.url = f"{BASE_URL}/exports/delete"