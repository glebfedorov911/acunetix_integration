from datetime import datetime

from pydantic import BaseModel, field_validator
from results.utils import calculate_md5_string


class TargetAgents(BaseModel):
    agent_id: str
    name: str | None = None

class DefaultOverride(BaseModel):
    auth: str | None = None
    scan: str | None = None

class Target(BaseModel):
    address: str
    description: str | None = None
    type: str | None = None
    criticality: int | None = None
    fqdn_status: str | None = None
    fqdn_tm_hash: str | None = None
    deleted_ad: datetime | None = None
    fqdn: str | None = None
    fqdn_hash: str | None = None
    default_scanning_profile_id: str | None = None
    agents: TargetAgents | None = None
    default_override: DefaultOverride | None = None

class AddTargetsDescriptor(BaseModel):
    targets: list[Target]
    groups: list[str] | None = []

class TargetIdList(BaseModel):
    target_id_list: list[str] | None = []

class ContinuousScanMode(BaseModel):
    enabled: bool

class SensorSecretContainer(BaseModel):
    secret: str | None = None

    @classmethod
    @field_validator("secret")
    def secret_validator(cls, value):
        return str(calculate_md5_string(value))

class TargetIdContainer(BaseModel):
    target_id: str | None = None

class UserCredentials(BaseModel):
    enabled: bool | None = None
    username: str | None = None
    password: str | None = None
    url: str | None = None

def validator_mixin(value, kind):
    if value not in kind:
        raise ValueError(f"kind must be one of {kind}")
    return value

class SiteLogin(BaseModel):
    kind: str
    credentials: UserCredentials | None = None

    @classmethod
    @field_validator("kind")
    def kind_validator(cls, value):
        KIND = ['none', 'automatic', 'sequence', 'oauth']

        return validator_mixin(value, KIND)

class SSHCredentials(BaseModel):
    kind: str | None = None
    username: str | None = None
    port: int | None = None
    password: str | None = None
    ssh_key: str | None = None
    key_password: str | None = None

    @classmethod
    @field_validator("kind")
    def kind_validator(cls, value):
        KIND = ['none', 'key', 'password']

        return validator_mixin(value, KIND)

class ProxySettings(BaseModel):
    protocol: str | None = None
    address: str | None = None
    port: int | None = None
    username: str | None = None
    password: str | None = None
    enabled: bool | None = None

class CustomCookies(BaseModel):
    cookie: str | None = None
    url: str | None = None

class TargetConfiguration(BaseModel):
    issue_tracker_id: str | None = None
    plugin_instance_id: str | None = None
    limit_crawler_scope: bool | None = None
    login: SiteLogin | None = None
    sensor: bool | None = None
    sensor_secret: str | None = None
    ssh_credentials: SSHCredentials | None = None
    proxy: ProxySettings | None = None
    authentication: UserCredentials | None = None
    client_certificate_password: str | None = None
    client_certificate_url: str | None = None
    scan_speed: str | None = None
    case_sensitive: str | None = None
    technologies: list[str] | None = None
    custom_headers: list[str] | None = None
    custom_cookies: list[CustomCookies] | None = None
    excluded_paths: list[str] | None = None
    user_agent: str | None = None
    debug: bool | None = None
    excluded_hours_id: str | None = None
    ad_blocker: bool | None = None
    restrict_scans_to_import_files: bool | None = None
    default_scanning_profile_id: str | None = None
    preseed_mode: str | None = None
    skip_login_form: bool | None = None

    @classmethod
    @field_validator("scan_speed")
    def scan_speed_validator(cls, value):
        SCAN_SPEED = ['slower', 'sequential', 'slow', 'moderate', 'fast']

        return validator_mixin(value, SCAN_SPEED)

    @classmethod
    @field_validator("case_sensitive")
    def case_sensitive_validator(cls, value):
        CASE_SENSITIVE = ['yes', 'no', 'auto']

        return validator_mixin(value, CASE_SENSITIVE)

class FileUploadDescriptor(BaseModel):
    name: str | None = None
    size: int | None = None

class ExcludedPathListUpdate(BaseModel):
    excluded_paths: list[str] | None = []