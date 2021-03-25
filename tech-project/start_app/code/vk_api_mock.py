import json

from flask import Flask

users = {}

vk_api_mock = Flask(__name__)


@vk_api_mock.route('/check/<username>')
def check(username):
    return str(users[username])


@vk_api_mock.route('/delete_id')
def delete_id():
    users.clear()
    return 'User`s id deleted!\n'


@vk_api_mock.route('/')
def index():
    return 'OKAY\n', 200


@vk_api_mock.route('/add_user/<username>')
def add_user(username):
    start_id = len(users) + 1
    users[username] = start_id
    return f'{username} add!'


@vk_api_mock.route('/vk_id/<username>')
def vk_id(username):
    if username in users.keys():
        return json.dumps({'vk_id': users[username]}), 200
    else:
        return json.dumps({}), 404


if __name__ == '__main__':
    vk_api_mock.run(host='0.0.0.0', port=7777)
