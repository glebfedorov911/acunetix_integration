from base import BASE_URL
from .api_vulnerabilities_mixin import ApiVulnerabilitiesMixin
from results.utils import VulnerabilitiesRecheck


class ApiVulnerabilitiesRecheck(ApiVulnerabilitiesMixin):


    def __init__(self, api_key: str, vulnerabilities_recheck: VulnerabilitiesRecheck):
        super().__init__("PUT", api_key, json=vulnerabilities_recheck.model_dump())
        self.url = f"{BASE_URL}/vulnerabilities/recheck"