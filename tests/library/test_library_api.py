import pytest
from dbks.client import Client
from dbks.library.api import LibraryAPI
from unittest.mock import patch


@pytest.mark.parametrize(
    "inputs, expect",
    [
        (
            {"func": "all_cluster_statuses"},
            {"method": "GET", "endpoint": "all-cluster-statuses"},
        ),
        (
            {"func": "cluster_status", "params": {"cluster_id": "1"}},
            {
                "method": "GET",
                "endpoint": "cluster-status",
                "params": {"cluster_id": "1"},
            },
        ),
        (
            {"func": "install", "json": {"a": "1"}},
            {"method": "POST", "endpoint": "install", "json": {"a": "1"}},
        ),
        (
            {"func": "uninstall", "json": {"a": "1"}},
            {"method": "POST", "endpoint": "uninstall", "json": {"a": "1"}},
        ),
    ],
)
def test_library_api(monkeypatch, inputs, expect):
    monkeypatch.setenv("DBC_TOKEN", "fake_token")
    with patch("dbks.client.Session.request") as mock:
        client = Client("databricks.com")
        api = LibraryAPI(client)
        getattr(api, inputs["func"])(
            params=inputs.get("params", None), json=inputs.get("json", None)
        )
        mock.assert_called_once_with(
            expect["method"],
            f"https://databricks.com/api/2.0/libraries/{expect['endpoint']}",
            params=expect.get("params", None),
            json=expect.get("json", None),
            headers={"Authorization": "Bearer fake_token"},
        )
