from dbks.workspace.api import WorkspaceAPI
from dbks.response_handler import ResponseHandler


class WorkspaceController:
    def __init__(self, api):
        if not isinstance(api, WorkspaceAPI):
            raise ValueError("Parameter must be an instance of WorkspaceAPI!")
        self.api = api

    @ResponseHandler
    def delete(self, path, recursive=True):
        self.api.delete(json={"path": path, "recursive": recursive})

    @ResponseHandler
    def export(self, path, format="SOURCE"):
        self.api.export(json={"path": path, "format": format})
