import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

DATA = []


class MockHandleRequests(BaseHTTPRequestHandler):

    def _send(self, status_code):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def do_POST(self):
        self._send(200)

        cont_length = int(self.headers['Content-Length'])
        data = self.rfile.read(cont_length).decode()
        if data in DATA:
            self.wfile.write('OK'.encode())
        else:
            self.wfile.write('DONT OK'.encode())

    def do_PUT(self):
        self._send(200)

        cont_length = int(self.headers['Content-Length'])
        DATA.append(self.rfile.read(cont_length).decode())

    def do_GET(self):
        if self.path == '/':
            self._send(200)
            self.wfile.write(json.dumps(DATA).encode())
        elif self.path == '/500':
            self._send(500)


class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.handler = MockHandleRequests
        self.handler.data = None
        self.server = HTTPServer((self.host, self.port), self.handler)

    def start(self):
        self.server.allow_reuse_address = True
        th = threading.Thread(target=self.server.serve_forever, daemon=True)
        th.start()

        return self.server

    def stop(self):
        self.server.server_close()
        self.server.shutdown()


if __name__ == '__main__':
    MyHTTPServer('127.0.0.1', 1052).start()
    while True:
        pass
