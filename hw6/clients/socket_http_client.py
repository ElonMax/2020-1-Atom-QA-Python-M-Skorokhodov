import json
import socket


class SocketClient:

    def __init__(self, host, port):
        self.target_host = host
        self.target_port = port

    def _connect(self):
        connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect.settimeout(0.1)

        count = 0
        while count < 3:
            try:
                connect.connect((self.target_host, self.target_port))
            except ConnectionRefusedError:
                count += 1
            break

        return connect

    def get_response(self, connect):
        total_data = []
        while True:
            data = connect.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                break

        connect.close()
        data = ''.join(total_data).splitlines()
        return {'status_code': int(data[0].split(' ')[1]), 'body': data[-1]}

    def to_json(self, dictionary):
        return json.dumps(dictionary, indent=4)

    def get(self, url):
        connect_get = self._connect()

        request = f'GET {url} HTTP/1.1\r\nHost:{self.target_host}\r\n\r\n'

        connect_get.send(request.encode())
        return self.get_response(connect_get)

    def post(self, url, data):
        connect_post = self._connect()

        en_data = data
        content_type = 'Content-Type:application/x-www-form-urlencoded'
        content_length = 'Content-Length:' + str(len(en_data))
        request = f'POST {url} HTTP/1.1\r\nHost:{self.target_host}\r\n{content_type}\r\n{content_length}\r\n\r\n' + en_data

        connect_post.send(request.encode())

        return self.get_response(connect_post)

    def put(self, url, data):
        connect_put = self._connect()

        en_data = data
        content_type = 'Content-Type: application/x-www-form-urlencoded'
        content_length = 'Content-Length:' + str(len(en_data))
        request = f'PUT {url} HTTP/1.1\r\nHost:{self.target_host}\r\n{content_type}\r\n{content_length}\r\n\r\n' + en_data

        connect_put.send(request.encode())

        return self.get_response(connect_put)


if __name__ == '__main__':
    client = SocketClient('127.0.0.1', 1050)
    output_get = client.get('/')
    print(client.to_json(output_get))
