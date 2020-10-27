import pytest
from dbks.client import Client
from dbks.cluster.api import ClusterAPI
from unittest.mock import patch


@pytest.mark.parametrize(
    "inputs, expect",
    [
        (
            {"func": "create", "json": {"a": "1"}},
            {"method": "POST", "endpoint": "create", "json": {"a": "1"}},
        ),
        (
            {"func": "edit", "json": {"a": "1"}},
            {"method": "POST", "endpoint": "edit", "json": {"a": "1"}},
        ),
        (
            {"func": "start", "json": {"a": "1"}},
            {"method": "POST", "endpoint": "start", "json": {"a": "1"}},
        ),
        (
            {"func": "restart", "json": {"a": "1"}},
            {"method": "POST", "endpoint": "restart", "json": {"a": "1"}},
        ),
        (
            {"func": "resize", "json": {"a": "1"}},
            {"method": "POST", "endpoint": "resize", "json": {"a": "1"}},
        ),
        (
            {"func": "terminate", "json": {"a": "1"}},
            {"method": "POST", "endpoint": "delete", "json": {"a": "1"}},
        ),
        (
            {"func": "delete", "json": {"a": "1"}},
            {"method": "POST", "endpoint": "permanent-delete", "json": {"a": "1"}},
        ),
        (
            {"func": "get", "params": {"a": "1"}},
            {"method": "GET", "endpoint": "get", "params": {"a": "1"}},
        ),
        (
            {"func": "pin", "json": {"a": "1"}},
            {"method": "POST", "endpoint": "pin", "json": {"a": "1"}},
        ),
        (
            {"func": "unpin", "json": {"a": "1"}},
            {"method": "POST", "endpoint": "unpin", "json": {"a": "1"}},
        ),
        ({"func": "list"}, {"method": "GET", "endpoint": "list"}),
        ({"func": "list_node_types"}, {"method": "GET", "endpoint": "list-node-types"}),
        ({"func": "runtime_versions"}, {"method": "GET", "endpoint": "spark-versions"}),
        ({"func": "list_zones"}, {"method": "GET", "endpoint": "list-zones"}),
        (
            {"func": "events", "json": {"a": "1"}},
            {"method": "POST", "endpoint": "events", "json": {"a": "1"}},
        ),
    ],
)
def test_cluster_api(monkeypatch, inputs, expect):
    monkeypatch.setenv("DBC_HOST", "fake_host.com")
    monkeypatch.setenv("DBC_TOKEN", "fake_token")
    with patch("dbks.client.Session.request") as mock:
        client = Client()
        api = ClusterAPI(client)
        getattr(api, inputs["func"])(
            params=inputs.get("params", None), json=inputs.get("json", None)
        )
        mock.assert_called_once_with(
            expect["method"],
            f"https://fake_host.com/api/2.0/clusters/{expect['endpoint']}",
            params=expect.get("params", None),
            json=expect.get("json", None),
            headers={"Authorization": "Bearer fake_token"},
        )
