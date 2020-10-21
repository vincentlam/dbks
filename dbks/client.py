import copy
import os
from requests import Session


class Client:
    def __init__(self, host: str, version: str = "2.0"):
        self.host = host
        self.version = version
        self.token = os.getenv(f"DBC_TOKEN", None)
        self.headers = {"Authorization": f"Bearer {self.token}"}
        self.session = Session()

    @property
    def url(self):
        return f"https://{self.host}/api/{self.version}"

    def call(self, method, endpoint, params={}, data={}, headers=None):
        if headers is None:
            headers = self.headers
        else:
            tmp_headers = copy.deepcopy(self.headers)
            tmp_headers.update(headers)
            headers = tmp_headers
        return self.session.request(
            method, self.url + endpoint, params=params, data=data, headers=headers
        )
