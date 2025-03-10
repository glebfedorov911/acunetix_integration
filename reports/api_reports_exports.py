from pydantic import BaseModel

from base import BASE_URL, API_KEY
from reports.api_reports_mixin import ApiReportsMixin
from .utils import ListTypeMixin


class ExportSource(ListTypeMixin):
    waf_id: str | None = None
    waf_name: str | None = None

class NewExport(BaseModel):
    export_id: str
    source: ExportSource

class ApiGetExportTypesReport(ApiReportsMixin):
    def __init__(self, api_key: str, new_export: NewExport):
        super().__init__("GET", api_key, json=new_export.model_dump())
        self.url = f"{BASE_URL}/export_types"