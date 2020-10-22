class ResponseHandler(object):
    def __init__(self):
        self

    def __getattribute__(self, attr):
        method = object.__getattribute__(self, attr)
        if not method:
            raise Exception("Method %s not implemented" % attr)
        if callable(method):
            print("I am:")
        return method
