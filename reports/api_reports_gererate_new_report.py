import uuid

from pydantic import BaseModel, field_validator

from reports.api_reports_mixin import ApiReportsMixin
from .utils import ListTypeMixin


class ReportSource(ListTypeMixin):
    description: str | None = None

class NewReport(BaseModel):
    template_id: uuid.UUID
    source: ReportSource


class ApiGenerateNewReport(ApiReportsMixin):


    def __init__(
            self,
            api_key: str,
            new_report: NewReport
    ):
        super().__init__("POST", api_key, json=new_report.model_dump())