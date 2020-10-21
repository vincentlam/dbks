from dbks.client import Client
from dbks.clusters.api import ClusterAPI
from unittest.mock import patch


def test_clusters_api_create(monkeypatch):
    monkeypatch.setenv("DBC_TOKEN", "fake_token")
    with patch("dbks.client.Session.request") as mock:
        client = Client("databricks.com")
        clusters_api = ClusterAPI(client)
        clusters_api.create({"a": "1"})
        mock.assert_called_once_with(
            "POST",
            "https://databricks.com/api/2.0/clusters/create",
            params={},
            data={"a": "1"},
            headers={"Authorization": "Bearer fake_token"},
        )
