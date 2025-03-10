import hashlib

from pydantic import BaseModel, field_validator


def calculate_md5_string(input_string):
    md5_hash = hashlib.md5()

    md5_hash.update(input_string.encode('utf-8'))

    return md5_hash.hexdigest()

class VulnRecheckMixin(BaseModel):
    ui_session_id: str | None = None

    @classmethod
    @field_validator("ui_session_id")
    def validate_status(cls, v):
        return str(calculate_md5_string(v))

class VulnerabilityRecheck(VulnRecheckMixin): ...

class VulnerabilitiesRecheck(VulnRecheckMixin):
    vuln_id_list: list[str]

class VulnerabilityStatus(BaseModel):
    status: str
    comment: str | None = None

    @classmethod
    @field_validator("status")
    def validate_status(cls, v):
        STATUS = ["fixed", "ignored", "open", "false_positive"]

        if v not in STATUS:
            raise ValueError(f"status must be one of {STATUS}")
        return v