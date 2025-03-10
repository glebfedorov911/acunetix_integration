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