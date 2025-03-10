from base import BASE_URL
from .api_results_mixin import ApiResultsMixin
from .utils import VulnRecheckMixin, VulnerabilitiesRecheck


class ApiRecheckScanSessionVunerabilitiesResults(ApiResultsMixin):
    def __init__(
            self,
            api_key: str,
            vulnerability_recheck: VulnerabilitiesRecheck,
            /,
            scan_id: str,
            result_id: str
    ):
        super().__init__("POST", api_key, json=vulnerability_recheck.model_dump())
        self.url = f"{BASE_URL}/scans/{scan_id}/results/{result_id}/vulnerabilities/recheck"