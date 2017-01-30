import os
from mpxapi import MPXApi
from mpxapi.entertainment import Programs

username = os.environ['MPX_USERNAME']
password = os.environ['MPX_PASSWORD']
account = os.environ['MPX_ACCOUNT']

api = MPXApi(username=username, password=password, account=account, tld="eu")
programs = Programs(api=api)

req = programs.get({"range": "-1"})
print req.text

api.sign_out()
