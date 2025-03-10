from pydantic import BaseModel


class IntegrationsVulnerabilityIdList(BaseModel):
    vuln_ids: list[str]