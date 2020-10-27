from dbks.client import Client
from unittest.mock import patch


def test_client_call(monkeypatch):
    monkeypatch.setenv("DBC_HOST", "fake_host.com")
    monkeypatch.setenv("DBC_TOKEN", "fake_token")
    with patch("dbks.client.Session.request") as mock:
        client = Client()
        client.call(method="GET", endpoint="/fake", params={"a": "1"})
        mock.assert_called_once_with(
            "GET",
            "https://fake_host.com/api/2.0/fake",
            params={"a": "1"},
            json=None,
            headers={"Authorization": "Bearer fake_token"},
        )
