class AccessTokenResponse:
    def __init__(self, **kwargs):
        self.token = kwargs.get('token')
        self.status_code = kwargs.get('status_code')
        self.credentials = kwargs.get('credentials')