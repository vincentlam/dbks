import pytest
from dbks.client import Client
from dbks.workspace.api import WorkspaceAPI
from unittest.mock import patch


@pytest.mark.parametrize(
    "inputs, expect, result",
    [
        (["delete", None, {"a": "1"}], ["POST", "delete", {}, {"a": "1"}], True),
        (["export", None, {"a": "1"}], ["GET", "export", {}, {"a": "1"}], True),
        (["get_status", None, {"a": "1"}], ["GET", "get-status", {}, {"a": "1"}], True),
        (["_import", None, {"a": "1"}], ["POST", "import", {}, {"a": "1"}], True),
        (["list", None, {"a": "1"}], ["GET", "list", {}, {"a": "1"}], True),
        (["mkdirs", None, {"a": "1"}], ["POST", "mkdirs", {}, {"a": "1"}], True),
    ],
)
def test_workspace_api(monkeypatch, inputs, expect, result):
    monkeypatch.setenv("DBC_TOKEN", "fake_token")
    with patch("dbks.client.Session.request") as mock:
        client = Client("databricks.com")
        api = WorkspaceAPI(client)
        getattr(api, inputs[0])(params=inputs[1], json=inputs[2])
        mock.assert_called_once_with(
            expect[0],
            f"https://databricks.com/api/2.0/workspace/{expect[1]}",
            params=expect[2],
            json=expect[3],
            headers={"Authorization": "Bearer fake_token"},
        )
