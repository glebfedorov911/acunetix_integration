from enum import Enum


class FactoryHttpClientException(Enum):
    NOT_FOUND_METHOD = "Not found method for this type request"

class HttpClientException(Enum):
    ERROR_SEND_REQUEST = "Error sending request"