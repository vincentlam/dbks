class ClusterAPI:
    def __init__(self, client):
        self.client = client

    def create(self, data):
        return self.client.call("POST", "/clusters/create", data=data)

    def edit(self, data):
        return self.client.call("POST", "/clusters/edit", data=data)

    def start(self, data):
        return self.client.call("POST", "/clusters/start", data=data)

    def restart(self, data):
        return self.client.call("POST", "/clusters/restart", data=data)

    def resize(self, data):
        return self.client.call("POST", "/clusters/resize", data=data)

    def terminate(self, data):
        return self.client.call("POST", "/clusters/delete", data=data)

    def delete(self, data):
        return self.client.call("POST", "/clusters/permanent-delete", data=data)

    def get(self, params):
        return self.client.call("GET", "/clusters/get", params=params)

    def pin(self, data):
        return self.client.call("POST", "/clusters/pin", data=data)

    def unpin(self, data):
        return self.client.call("POST", "/clusters/unpin", data=data)

    def list(self):
        return self.client.call("GET", "/clusters/list")

    def list_node_types(self):
        return self.client.call("GET", "/clusters/list-node-types")

    def runtime_versions(self):
        return self.client.call("GET", "/clusters/spark-versions")

    def list_zones(self):
        return self.client.call("GET", "/clusters/list-zones")

    def events(self, data):
        return self.client.call("POST", "/clusters/events", data=data)
