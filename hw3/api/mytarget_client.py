import json
from urllib.parse import urljoin
import requests


class ResponseStatusCodeException(Exception):
    pass


class ApiClient:

    def __init__(self, user, password):
        self.base_url = 'https://target.my.com/'
        self.session = requests.Session()
        self.user = user
        self.password = password
        self.login()

    def _get_csrf_token(self):
        self._request('GET', 'https://target.my.com/csrf')
        return self.session.cookies['csrftoken']

    def _request(self, method, location, status_code=200, headers=None, data=None):
        url = urljoin(self.base_url, location)

        response = self.session.request(method, url, headers=headers, data=data)

        if response.status_code != status_code:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.reason} for URL: {url}')

        return response

    def login(self):
        location = 'https://auth-ac.my.com/auth'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://target.my.com/'
        }

        data = {
            'email': self.user,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/'
        }

        response = self._request('POST', location, headers=headers, data=data)

        return response

    def create_segment(self, name='create_segment'):
        location = 'api/v2/remarketing/segments.json?fields=relations__object_type,' \
                   'relations__object_id,relations__params,relations_count,id,name,' \
                   'pass_condition,created,campaign_ids,users,flags'

        headers = {
            'X-CSRFToken': self._get_csrf_token()
        }

        data = json.dumps({
                "name": name,
                "pass_condition": 1,
                "relations": [
                    {
                        "object_type": "remarketing_player",
                        "params": {
                            "type": "positive",
                            "left": 365,
                            "right": 0
                        }
                    }
                ],
                "logicType": "or"
        })

        response = self._request('POST', location, data=data, headers=headers)

        return response.json()['id']

    def check_segment(self, segment_id):
        location = f'api/v2/remarketing/segments/{segment_id}' \
                   '/relations.json?fields=id,params,object_type,object_id&_=1603048890574'

        self._request('GET', location, status_code=200)

    def delete_segment(self, segment_id):
        location = f'api/v2/remarketing/segments/{segment_id}.json'

        headers = {
            'Referer': 'https://target.my.com/segments/segments_list',
            'X-CSRFToken': self._get_csrf_token()
        }

        self._request('DELETE', location, status_code=204, headers=headers)
