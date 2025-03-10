from pydantic import BaseModel

from target.utils import ProxySettings


class Proxy(BaseModel):
    proxy_type: str | None = None
    settings: ProxySettings | None = None

class WAFConfig(BaseModel):
    platform: str | None = None
    acl_name: str
    access_key_id: str
    secret_key: str
    scope: str
    region: str | None = None
    acl_id: str
    proxy: Proxy

class WAFEntry(WAFConfig):
    waf_id: str | None = None
    name: str | None = None