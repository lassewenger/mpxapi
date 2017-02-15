class FeedConfig:
    def __init__(self, api):
        self.schema = "2.2.0"
        self.service = "Feeds Data Service"
        self.path = "/data/FeedConfig"
        self.api = api

    def get(self, params):
        return self.api.command(service=self.service, path=self.path, method="GET", params=self.apply_schema(params))

    def get_by_id(self, id, params = {}):
        return self.api.command(service=self.service, path=self.path + '/' + str(id), method="GET",
                                params=self.apply_schema(params))

    def apply_schema(self, params):
        params.update({"schema": self.schema})
        return params
