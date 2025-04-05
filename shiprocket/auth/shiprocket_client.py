import os
import requests
from cachetools import TTLCache
from .credentials import Credentials
from .access_token_response import AccessTokenResponse
from .exceptions import AuthorizationError


class ShiprocketClient:
    def __init__(self, credentials=None):
        self.base_url = "https://apiv2.shiprocket.in/v1/external/"
        self.cred = Credentials(credentials)
        self.cache = TTLCache(maxsize=1, ttl=3200)
        self.token = self.get_auth()

    def _request(self, url, data):
        response = requests.post(url, data=data)
        response_data = response.json()
        if response.status_code != 200:
            error_message = str(response.content)
            error_code = response.status_code
            raise AuthorizationError(
                error_code, error_message, response.status_code)
        return response_data

    def get_auth(self) -> AccessTokenResponse:
        if 'token' in self.cache:  # If the token is in the cache and hasn't expired
            return self.cache['token']
        auth_url = f"{self.base_url}auth/login/"
        access_token = self._request(auth_url, self.cred.credentials)
        token = AccessTokenResponse(**access_token)
        self.cache['token'] = token
        return token

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token.token}"
        }
