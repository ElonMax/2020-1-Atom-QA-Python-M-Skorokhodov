import json
from urllib.parse import urljoin

import allure
import requests


class ResponseStatusCodeException(Exception):
    pass


class ApiClient:

    def __init__(self):
        self.base_url = 'http://0.0.0.0:7070'
        self.session = requests.Session()

    def _request(self, method, location, status_code=200, headers=None, data=None):
        url = urljoin(self.base_url, location)

        response = self.session.request(method, url, headers=headers, data=data)

        if response.status_code != status_code:
            if method == 'POST':
                allure.attach(name='request',
                              body=json.dumps({'url': response.request.url,
                                               'method': response.request.method,
                                               'body': json.loads(response.request.body)
                                               }, indent=4)
                              )
            elif method == 'GET':
                allure.attach(name='request',
                              body=json.dumps({'url': response.request.url,
                                               'method': response.request.method,
                                               }, indent=4)
                              )
            allure.attach(name='response',
                          body=json.dumps({'body': response.text,
                                           'status_code': response.status_code
                                           }, indent=4)
                          )
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.reason} for URL: {url}!')

        return response

    def login(self, username, password, status_code=200):
        location = '/login'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            'username': username,
            'password': password,
            'submit': 'Login'
        }

        response = self._request('POST', location, headers=headers, data=data, status_code=status_code)

        return response

    def status(self, status_code=200):
        location = '/status'

        response = self._request('GET', location, status_code=status_code)

        return response

    def delete_user(self, username, status_code=204):
        location = f'/api/del_user/{username}'

        response = self._request('GET', location, status_code=status_code)

        return response

    def add_user(self, username, password, email, status_code=201):
        location = '/api/add_user'

        headers = {
            'Content-Type': 'application/json'
        }

        data = json.dumps({
            "username": username,
            "password": password,
            "email": email
        })

        response = self._request('POST', location, headers=headers, data=data, status_code=status_code)

        return response

    def block_user(self, username):
        location = f'/api/block_user/{username}'

        response = self._request('GET', location)

        return response

    def unblock_user(self, username):
        location = f'/api/accept_user/{username}'

        response = self._request('GET', location)

        return response

    def bad_request_add_user(self, username, status_code=200):
        location = '/api/add_user'

        headers = {
            'Content-Type': 'application/json'
        }

        data = json.dumps({
            "username": username
        })

        response = self._request('POST', location, headers=headers, data=data, status_code=status_code)

        return response
