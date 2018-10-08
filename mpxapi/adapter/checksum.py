from mpxapi.api_base import ApiBase


class Checksum(ApiBase):
    def __init__(self, api):
        ApiBase.__init__(self, api)

        self.schema = "2.15.0"
        self.searchSchema = "1.3.0"
        self.service = "Checksum Data Service"
        self.path = "/data/Checksum"
