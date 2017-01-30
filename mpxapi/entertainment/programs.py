class Programs:
    def __init__(self, api):
        self.schema = "2.15.0"
        self.searchSchema = "1.3.0"
        self.service = "Entertainment Data Service"
        self.path = "/data/Program"
        self.api = api

    def get(self, params):
        return self.api.command(service=self.service, path=self.path, method="GET", params=self.apply_schema(params))

    def apply_schema(self, params):
        params.update({"schema": self.schema})
        params.update({"searchSchema": self.searchSchema})
        return params