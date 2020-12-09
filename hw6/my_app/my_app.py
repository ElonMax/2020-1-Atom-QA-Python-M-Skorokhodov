import threading
from flask import Flask, request

from clients.socket_http_client import SocketClient

app = Flask(__name__)


def run_app():
    server = threading.Thread(target=app.run, kwargs={
        'host': '127.0.0.1',
        'port': 1050
    })

    server.start()

    return server


def shutdown_app():
    terminate = request.environ.get('werkzeug.server.shutdown')
    if terminate:
        terminate()


@app.route('/', methods=['GET'])
def index():
    try:
        client = SocketClient('127.0.0.1', 1052)
        output_get = client.get('/')
        return output_get['body']
    except BrokenPipeError:
        return 'Mock is down'


@app.route('/data_post', methods=['POST'])
def data_post():
    client = SocketClient('127.0.0.1', 1052)
    output_post = client.post('/data_post', request.form['name'])

    return output_post['body']


@app.route('/data_put', methods=['PUT'])
def data_put():
    client = SocketClient('127.0.0.1', 1052)
    client.put('/data_put', request.form['name'])
    return ''


@app.route('/500', methods=['GET'])
def error500():
    client = SocketClient('127.0.0.1', 1052)
    data = client.get('/500')
    if data['status_code'] == 500:
        return '', 424
    else:
        return 'unknown'


@app.route('/shutdown')
def shutdown():
    shutdown_app()


if __name__ == '__main__':
    run_app()
