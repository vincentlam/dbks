import pytest
from dbks.client import Client
from dbks.library.api import LibraryAPI
from unittest.mock import patch


@pytest.mark.parametrize(
    "inputs, expect, result",
    [
        (
            ["all_cluster_statuses", None, None],
            ["GET", "all-cluster-statuses", {}, {}],
            True,
        ),
        (
            ["cluster_status", {"cluster_id": "1"}, None],
            ["GET", "cluster-status", {"cluster_id": "1"}, {}],
            True,
        ),
        (["install", None, {"a": "1"}], ["POST", "install", {}, {"a": "1"}], True),
        (["uninstall", None, {"a": "1"}], ["POST", "uninstall", {}, {"a": "1"}], True),
    ],
)
def test_library_api(monkeypatch, inputs, expect, result):
    monkeypatch.setenv("DBC_TOKEN", "fake_token")
    with patch("dbks.client.Session.request") as mock:
        client = Client("databricks.com")
        api = LibraryAPI(client)
        getattr(api, inputs[0])(params=inputs[1], json=inputs[2])
        mock.assert_called_once_with(
            expect[0],
            f"https://databricks.com/api/2.0/libraries/{expect[1]}",
            params=expect[2],
            json=expect[3],
            headers={"Authorization": "Bearer fake_token"},
        )
