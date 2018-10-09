import os
import logging
import time
from mpxapi import MPXApi
from mpxapi.entertainment import Program
from mpxapi.adapter import Checksum

logging.basicConfig(level=logging.DEBUG)

username = os.environ["MPX_USERNAME"]
password = os.environ["MPX_PASSWORD"]
account = os.environ["MPX_ACCOUNT"]

api = MPXApi(username=username, password=password, account=account, tld="eu")
program = Program(api=api)

req = program.get({"range": "-1", "fields": "id,title"})
print(req.text)

api.sign_out()

time.sleep(2)

params = {"schema": 1.0, "form": "json"}
req = api.command(
    service="User Data Service",
    path="/web/Self/getSelfId",
    method="GET",
    params=params,
)

media = "http://data.media.theplatform.eu/media/data/Media/246212677354"

params = {"schema": "1.2.0", "form": "json", "byMediaId": media}
req = api.command(
    service="Ingest Data Service",
    path="/data/Checksum",
    method="GET",
    params=params,
)

print(req.text)

checksum = Checksum(api=api).get(
    params={'byMediaId': media}
)

print(checksum.json())
