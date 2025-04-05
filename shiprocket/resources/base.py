import requests
class Resource(object):

    def __init__(self, client=None):
        self.client = client

    def _request(self, method, path, params=None, data=None, files=None):
            base_url=self.client.base_url
            headers=self.client.get_headers()
            url = f"{base_url}{path}"
            response = requests.request(
                method, url, headers=headers, json=data, params=params, files=files)
            return response # returning the response object