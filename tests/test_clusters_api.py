from _pytest.mark import param
import pytest
from dbks.client import Client
from dbks.clusters.api import ClusterAPI
from unittest.mock import patch


@pytest.mark.parametrize(
    "inputs, expect, result",
    [
        (["create", None, {"a": "1"}], ["POST", "create", {}, {"a": "1"}], True),
        (["edit", None, {"a": "1"}], ["POST", "edit", {}, {"a": "1"}], True),
        (["start", None, {"a": "1"}], ["POST", "start", {}, {"a": "1"}], True),
        (["restart", None, {"a": "1"}], ["POST", "restart", {}, {"a": "1"}], True),
        (["resize", None, {"a": "1"}], ["POST", "resize", {}, {"a": "1"}], True),
        (["terminate", None, {"a": "1"}], ["POST", "delete", {}, {"a": "1"}], True),
        (
            ["delete", None, {"a": "1"}],
            ["POST", "permanent-delete", {}, {"a": "1"}],
            True,
        ),
        (["get", {"a": "1"}, None], ["GET", "get", {"a": "1"}, {}], True),
        (["pin", None, {"a": "1"}], ["POST", "pin", {}, {"a": "1"}], True),
        (["unpin", None, {"a": "1"}], ["POST", "unpin", {}, {"a": "1"}], True),
        (["list", None, None], ["GET", "list", {}, {}], True),
        (["list_node_types", None, None], ["GET", "list-node-types", {}, {}], True),
        (["runtime_versions", None, None], ["GET", "spark-versions", {}, {}], True),
        (["list_zones", None, None], ["GET", "list-zones", {}, {}], True),
        (["events", None, {"a": "1"}], ["POST", "events", {}, {"a": "1"}], True),
    ],
)
def test_clusters_api(monkeypatch, inputs, expect, result):
    monkeypatch.setenv("DBC_TOKEN", "fake_token")
    with patch("dbks.client.Session.request") as mock:
        client = Client("databricks.com")
        clusters_api = ClusterAPI(client)
        getattr(clusters_api, inputs[0])(params=inputs[1], data=inputs[2])
        mock.assert_called_once_with(
            expect[0],
            f"https://databricks.com/api/2.0/clusters/{expect[1]}",
            params=expect[2],
            data=expect[3],
            headers={"Authorization": "Bearer fake_token"},
        )
