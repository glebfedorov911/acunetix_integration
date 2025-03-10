

class HttpError(Exception):

    def __init__(
            self,
            status_code: int,
            details: str,
    ):
        self.status_code = status_code
        self.details = details
        super().__init__(f"PROBLEM | {status_code}, {self.details}")

class HttpErrorBadRequest(HttpError):
    def __init__(self):
        super().__init__(400, "Bad Request")

class HttpErrorUnauthorized(HttpError):
    def __init__(self):
        super().__init__(401, "Unauthorized")

class HttpErrorForbidden(HttpError):
    def __init__(self):
        super().__init__(403, "Forbidden")

class HttpErrorNotFound(HttpError):
    def __init__(self):
        super().__init__(404, "Not Found")

class HttpErrorInternalError(HttpError):
    def __init__(self):
        super().__init__(500, "Internal Server Error. Try edit your body of request")

class HttpErrorRegistry:
    _registry = {}

    @classmethod
    def register_error(cls, status_code: int, error_class):
        cls._registry[status_code] = error_class

    @classmethod
    def get_error(cls, status_code: int):
        return cls._registry.get(status_code)

class HttpErrorFabric:

    @staticmethod
    def create_error(status_code: int, details: str):
        error_class = HttpErrorRegistry.get_error(status_code)
        if error_class:
            return error_class()
        return HttpError(status_code, details)

HttpErrorRegistry.register_error(400, HttpErrorBadRequest)
HttpErrorRegistry.register_error(401, HttpErrorUnauthorized)
HttpErrorRegistry.register_error(403, HttpErrorForbidden)
HttpErrorRegistry.register_error(404, HttpErrorNotFound)
HttpErrorRegistry.register_error(500, HttpErrorInternalError)
