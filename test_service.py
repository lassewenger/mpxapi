import os
from mpxapi import MPXApi

username = os.environ['MPX_USERNAME']
password = os.environ['MPX_PASSWORD']
account = os.environ['MPX_ACCOUNT']

api = MPXApi(username=username, password=password, account=account, tld="eu")

params= {"schema": "2.15.0", "searchSchema": "1.3.0", "range": "-1", "pretty": "true"}
req = api.command(service="Entertainment Data Service", path="/data/Program", method="GET", params=params)
print req.text

api.sign_out()
