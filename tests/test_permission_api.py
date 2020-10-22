import pytest
from dbks.client import Client
from dbks.permission.api import PermissionAPI
from unittest.mock import patch


@pytest.mark.parametrize(
    "inputs, expect, result",
    [
        (
            ["get_cluster_permission_levels", {"cluster_id": "1"}, None],
            ["GET", "clusters/1/permissionLevels", {}, {}],
            True,
        ),
        (
            ["get_cluster_permissions", {"cluster_id": "1"}, None],
            ["GET", "clusters/1", {}, {}],
            True,
        ),
        (
            ["update_cluster_permissions", {"cluster_id": "1"}, {"a": "1"}],
            ["PATCH", "clusters/1", {}, {"a": "1"}],
            True,
        ),
        (
            ["replace_cluster_permissions", {"cluster_id": "1"}, {"a": "1"}],
            ["PUT", "clusters/1", {}, {"a": "1"}],
            True,
        ),
        (
            ["get_directory_permission_levels", {"directory_id": "1"}, None],
            ["GET", "directories/1/permissionLevels", {}, {}],
            True,
        ),
        (
            ["get_directory_permissions", {"directory_id": "1"}, None],
            ["GET", "directories/1", {}, {}],
            True,
        ),
        (
            ["update_directory_permissions", {"directory_id": "1"}, {"a": "1"}],
            ["PATCH", "directories/1", {}, {"a": "1"}],
            True,
        ),
        (
            ["replace_directory_permissions", {"directory_id": "1"}, {"a": "1"}],
            ["PUT", "directories/1", {}, {"a": "1"}],
            True,
        ),
    ],
)
def test_permission_api(monkeypatch, inputs, expect, result):
    monkeypatch.setenv("DBC_TOKEN", "fake_token")
    with patch("dbks.client.Session.request") as mock:
        client = Client("databricks.com")
        api = PermissionAPI(client)
        getattr(api, inputs[0])(params=inputs[1], json=inputs[2])
        mock.assert_called_once_with(
            expect[0],
            f"https://databricks.com/api/2.0/permissions/{expect[1]}",
            params=expect[2],
            json=expect[3],
            headers={"Authorization": "Bearer fake_token"},
        )
