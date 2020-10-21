class ClusterAPI:
    def __init__(self, client):
        self.client = client

    def create(self, data):
        return self.client.call("POST", "/clusters/create", data=data)
