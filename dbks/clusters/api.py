class ClusterAPI:
    def __init__(self, client):
        self.client = client

    def create(self, params=None, data=None):
        return self.client.call("POST", "/clusters/create", data=data)

    def edit(self, params=None, data=None):
        return self.client.call("POST", "/clusters/edit", data=data)

    def start(self, params=None, data=None):
        return self.client.call("POST", "/clusters/start", data=data)

    def restart(self, params=None, data=None):
        return self.client.call("POST", "/clusters/restart", data=data)

    def resize(self, params=None, data=None):
        return self.client.call("POST", "/clusters/resize", data=data)

    def terminate(self, params=None, data=None):
        return self.client.call("POST", "/clusters/delete", data=data)

    def delete(self, params=None, data=None):
        return self.client.call("POST", "/clusters/permanent-delete", data=data)

    def get(self, params=None, data=None):
        return self.client.call("GET", "/clusters/get", params=params)

    def pin(self, params=None, data=None):
        return self.client.call("POST", "/clusters/pin", data=data)

    def unpin(self, params=None, data=None):
        return self.client.call("POST", "/clusters/unpin", data=data)

    def list(self, params=None, data=None):
        return self.client.call("GET", "/clusters/list")

    def list_node_types(self, params=None, data=None):
        return self.client.call("GET", "/clusters/list-node-types")

    def runtime_versions(self, params=None, data=None):
        return self.client.call("GET", "/clusters/spark-versions")

    def list_zones(self, params=None, data=None):
        return self.client.call("GET", "/clusters/list-zones")

    def events(self, params=None, data=None):
        return self.client.call("POST", "/clusters/events", data=data)
