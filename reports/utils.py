from pydantic import BaseModel, field_validator


class ListTypeMixin(BaseModel):
    id_list: list[str] | None = None
    list_type: str

    @classmethod
    @field_validator('list_type')
    def list_type_validator(cls, value):
        LIST_TYPE = [
            "scan_result_pair", "scan_pair", "scan_vulnerabilities",
            "vulnerabilities", "scan_result", "scans", "groups",
            "targets", "all_vulnerabilities"
        ]

        if value not in LIST_TYPE:
            raise ValueError(f"List type {value} not valid")
        return value

class ReportIdList(BaseModel):
    report_id_list: list[str]