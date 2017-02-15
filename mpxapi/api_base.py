import json


class ApiBase:
    def __init__(self, api):
        self.api = api

    def get(self, params):
        return self.api.command(service=self.service, path=self.path, method="GET", params=self.apply_schema(params))

    def get_by_id(self, id, params={}):
        return self.api.command(service=self.service, path=self.path + '/' + str(id), method="GET",
                                params=self.apply_schema(params))

    def put(self, data, params={}):
        return self.api.command(service=self.service, path=self.path + '/', method="PUT",
                                params=self.apply_schema(params),
                                data=json.dumps(data, sort_keys=True))

    def post(self, data, params={}):
        return self.api.command(service=self.service, path=self.path + '/', method="POST",
                                params=self.apply_schema(params),
                                data=json.dumps(data, sort_keys=True))

    def apply_schema(self, params):
        if self.schema:
            params.update({"schema": self.schema})
        if self.searchSchema:
            params.update({"searchSchema": self.searchSchema})
        return params
