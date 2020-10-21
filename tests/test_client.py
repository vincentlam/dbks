from dbks.client import Client
from unittest.mock import patch


def test_client_call(monkeypatch):
    monkeypatch.setenv("DBC_TOKEN", "fake_token")
    with patch("dbks.client.Session.request") as mock:
        client = Client("databricks.com")
        client.call("GET", "/fake", {"a": "1"})
        mock.assert_called_once_with(
            "GET",
            "https://databricks.com/api/2.0/fake",
            params={"a": "1"},
            data={},
            headers={"Authorization": "Bearer fake_token"},
        )
