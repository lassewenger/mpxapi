import json


class ApiBase:
    def __init__(self, api):
        self.api = api

        # Setup variables to be modified by extending classes
        self.service = None
        self.path = None
        self.schema = None
        self.searchSchema = None

    def get(self, params):
        return self.api.command(service=self.service, path=self.path, method="GET", params=self.apply_schema(params))

    def get_by_id(self, entity_id, params=None):
        if not params:
            params = {}
        return self.api.command(service=self.service, path=self.path + '/' + str(entity_id), method="GET",
                                params=self.apply_schema(params))

    def put(self, data, params=None):
        if not params:
            params = {}
        return self.api.command(service=self.service, path=self.path + '/', method="PUT",
                                params=self.apply_schema(params),
                                data=json.dumps(data, sort_keys=True))

    def post(self, data, params=None):
        if not params:
            params = {}
        return self.api.command(service=self.service, path=self.path + '/', method="POST",
                                params=self.apply_schema(params),
                                data=json.dumps(data, sort_keys=True))

    def apply_schema(self, params):
        if self.schema:
            params.update({"schema": self.schema})
        if self.searchSchema:
            params.update({"searchSchema": self.searchSchema})
        return params
