from .exceptions import InvalidCredentialsException, InvalidServiceException
import requests
import logging
from requests.auth import HTTPBasicAuth

REGISTRY_URL = "https://access.auth.theplatform.{tld}/web/Registry/resolveDomain"
SIGN_IN_URL = "https://identity.auth.theplatform.{tld}/idm/web/Authentication/signIn"
SIGN_OUT_URL = "https://identity.auth.theplatform.{tld}/idm/web/Authentication/signOut"


class MPXApi:
    def __init__(self, username, password, account, tld):
        self.username = username
        self.password = password
        self.account = account
        self.tld = tld
        self.token = None
        self.registry = None

        self.sign_in()
        self.get_registry()

    def sign_in(self):
        # Ask for a default timeout of 1 hour, and 10 minutes of idle timeout
        params = {'schema': '1.1', '_duration': '3600000', '_idleTimeout': '600000'}
        headers = {'Content-Type': 'application/json'}
        auth = HTTPBasicAuth(username=self.username, password=self.password)
        r = requests.get(SIGN_IN_URL.format(tld=self.tld), params=params,
                         headers=headers, auth=auth)

        if r.status_code == 200:
            auth_data = r.json()['signInResponse']
            self.token = auth_data['token']
        else:
            raise InvalidCredentialsException('Unable to auth for user: ' + self.username)

    def sign_out(self):
        params = {'schema': '1.1', '_token': self.token}
        headers = {'Content-Type': 'application/json'}
        req = requests.get(SIGN_OUT_URL.format(tld=self.tld), params=params, headers=headers)

    def get_registry(self):
        logging.debug("Fetching service registry from %s" % REGISTRY_URL.format(tld=self.tld))
        params = {"schema": "1.1", "form": "json",
                  "_accountId": "http://access.auth.theplatform.com/data/Account/" + self.account}
        registry_request = self.raw_command(method="GET", url=REGISTRY_URL.format(tld=self.tld), params=params)
        self.registry = registry_request.json()['resolveDomainResponse']

    def raw_command(self, method, url, params, data=None):
        params.update({"account": self.account})
        params.update({"token": self.token})
        if not "form" in params:
            params.update({"form": "cjson"})
            params.update({"pretty": "true"})

        req = requests.request(method, url, params=params, data=data)

        # check if we maybe have an expired token
        if "AuthenticationException" in req.text or "InvalidTokenException" in req.text:
            logging.debug("We encountered an AuthenticationException or InvalidTokenException, re-signing in")
            self.sign_in()
            return self.raw_command(method, url, params, data)

        return req

    def command(self, service, path, method, params, data=None):
        url = ""
        try:
            url = self.registry[service]
        except KeyError:
            raise InvalidServiceException("Service " + service + " could not be found")
        url += path

        return self.raw_command(method=method, url=url, params=params, data=data)
