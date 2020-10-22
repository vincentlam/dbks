import pytest
from dbks.client import Client
from dbks.permission.api import PermissionAPI
from unittest.mock import patch


@pytest.mark.parametrize(
    "inputs, expect",
    [
        (
            {"func": "get_cluster_permission_levels", "params": {"cluster_id": "1"}},
            {"method": "GET", "endpoint": "clusters/1/permissionLevels"},
        ),
        (
            {"func": "get_cluster_permissions", "params": {"cluster_id": "1"}},
            {"method": "GET", "endpoint": "clusters/1"},
        ),
        (
            {
                "func": "update_cluster_permissions",
                "params": {"cluster_id": "1"},
                "json": {"a": "1"},
            },
            {"method": "PATCH", "endpoint": "clusters/1", "json": {"a": "1"}},
        ),
        (
            {
                "func": "replace_cluster_permissions",
                "params": {"cluster_id": "1"},
                "json": {"a": "1"},
            },
            {"method": "PUT", "endpoint": "clusters/1", "json": {"a": "1"}},
        ),
        (
            {
                "func": "get_directory_permission_levels",
                "params": {"directory_id": "1"},
            },
            {"method": "GET", "endpoint": "directories/1/permissionLevels"},
        ),
        (
            {"func": "get_directory_permissions", "params": {"directory_id": "1"}},
            {"method": "GET", "endpoint": "directories/1"},
        ),
        (
            {
                "func": "update_directory_permissions",
                "params": {"directory_id": "1"},
                "json": {"a": "1"},
            },
            {"method": "PATCH", "endpoint": "directories/1", "json": {"a": "1"}},
        ),
        (
            {
                "func": "replace_directory_permissions",
                "params": {"directory_id": "1"},
                "json": {"a": "1"},
            },
            {"method": "PUT", "endpoint": "directories/1", "json": {"a": "1"}},
        ),
    ],
)
def test_permission_api(monkeypatch, inputs, expect):
    monkeypatch.setenv("DBC_TOKEN", "fake_token")
    with patch("dbks.client.Session.request") as mock:
        client = Client("databricks.com")
        api = PermissionAPI(client)
        getattr(api, inputs["func"])(
            params=inputs.get("params", None), json=inputs.get("json", None)
        )
        mock.assert_called_once_with(
            expect["method"],
            f"https://databricks.com/api/2.0/permissions/{expect['endpoint']}",
            params=expect.get("params", None),
            json=expect.get("json", None),
            headers={"Authorization": "Bearer fake_token"},
        )
