import logging.config
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "detailed": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
        "simple": {
            "format": "%(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": "INFO"
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "app.log",
            "formatter": "detailed",
            "level": "DEBUG",
        },
    },
    "loggers": {
        "app": {
            "handlers": ["file", "console"],
            "level": "DEBUG",
            "propagate": False
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("app")