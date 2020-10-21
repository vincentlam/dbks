class Endpoint:
    mapping = {
        "clusters": {
            "create": "POST",
            "edit": "POST",
            "start": "POST",
            "restart": "POST",
            "resize": "POST",
            "delete": "POST",
            "permanent-delete": "POST",
            "get": "GET",
            "pin": "POST",
            "unpin": "POST",
            "list": "GET",
            "list-node-types": "GET",
            "spark-versions": "GET",
            "list-zones": "GET",
            "events": "POST",
        },
        "jobs": {"create": "POST", "list": "GET", "delete": "POST"},
    }

    def __init__(self, resource: str, action: str, **parameters):
        self.resource = resource
        self.action = action
        self.parameters = parameters
        if resource not in self.mapping.keys():
            raise ValueError(
                f'Parameter "resource" must be one of {list(self.mapping.keys())}!'
            )
        if action not in self.mapping[resource]:
            raise ValueError(f'Endpoint "/{resource}/{action}" not defined in mapping!')

    @property
    def string(self):
        return f"/{self.resource}/{self.action}"

    @property
    def method(self):
        return self.mapping[self.resource][self.action]
