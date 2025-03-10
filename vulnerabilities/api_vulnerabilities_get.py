from .api_vulnerabilities_mixin import ApiVulnerabilitiesMixin


class ApiVulnerabilitiesGet(ApiVulnerabilitiesMixin):


    def __init__(self, api_key: str):
        super().__init__("GET", api_key)