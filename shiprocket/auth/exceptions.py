class AuthorizationError(Exception):
    def __init__(self, error_code, error_msg, status_code):
        self.error_code = error_code
        self.message = error_msg
        self.status_code = status_code
