import os, logging, time
from mpxapi import MPXApi
from mpxapi.entertainment import Program

logging.basicConfig(level=logging.DEBUG)

username = os.environ['MPX_USERNAME']
password = os.environ['MPX_PASSWORD']
account = os.environ['MPX_ACCOUNT']

api = MPXApi(username=username, password=password, account=account, tld="eu")
program = Program(api=api)

req = program.get({"range": "-1", "fields": "id,title"})
print(req.text)

api.sign_out()

time.sleep(2)

params = {'schema': 1.0, 'form': 'json'}
req = api.command(service="User Data Service", path="/web/Self/getSelfId", method="GET", params=params)
print(req.text)
