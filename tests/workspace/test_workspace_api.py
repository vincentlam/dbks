import pytest
from dbks.client import Client
from dbks.workspace.api import WorkspaceAPI
from unittest.mock import patch


@pytest.mark.parametrize(
    "inputs, expect",
    [
        (
            {"func": "delete", "json": {"a": "1"}},
            {"method": "POST", "endpoint": "delete", "json": {"a": "1"}},
        ),
        (
            {"func": "export", "json": {"a": "1"}},
            {"method": "GET", "endpoint": "export", "json": {"a": "1"}},
        ),
        (
            {"func": "get_status", "json": {"a": "1"}},
            {"method": "GET", "endpoint": "get-status", "json": {"a": "1"}},
        ),
        (
            {"func": "_import", "json": {"a": "1"}},
            {"method": "POST", "endpoint": "import", "json": {"a": "1"}},
        ),
        (
            {"func": "list", "json": {"a": "1"}},
            {"method": "GET", "endpoint": "list", "json": {"a": "1"}},
        ),
        (
            {"func": "mkdirs", "json": {"a": "1"}},
            {"method": "POST", "endpoint": "mkdirs", "json": {"a": "1"}},
        ),
    ],
)
def test_workspace_api(monkeypatch, inputs, expect):
    monkeypatch.setenv("DBC_TOKEN", "fake_token")
    with patch("dbks.client.Session.request") as mock:
        client = Client("databricks.com")
        api = WorkspaceAPI(client)
        getattr(api, inputs["func"])(
            params=inputs.get("params", None), json=inputs.get("json", None)
        )
        mock.assert_called_once_with(
            expect["method"],
            f"https://databricks.com/api/2.0/workspace/{expect['endpoint']}",
            params=expect.get("params", None),
            json=expect.get("json", None),
            headers={"Authorization": "Bearer fake_token"},
        )
