import requests

from base import BASE_URL
from custom_logger import logger


def is_available_acunetix_api() -> None:
    try:
        logger.info("Trying to connect to Acunetix API")
        response = requests.get(BASE_URL, timeout=5, verify=False)
        response.raise_for_status()
        logger.info("Success connection to Acunetix API")
    except Exception as e:
        logger.exception(e)
        raise Exception("Acunetix API is not available")

is_available_acunetix_api()