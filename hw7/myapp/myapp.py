from flask import Flask

myapp = Flask(__name__)


@myapp.route('/')
def start_page():
    return 'Welcome to start page!'


@myapp.route('/shop')
def shop():
    return 'This is shop page'


@myapp.route('/shop/buy')
def buy():
    return 'Thank you for your purchase!'


@myapp.route('/downloads')
def downloads():
    return 'This is downloads page'


@myapp.route('/downloads/gets')
def gets():
    return 'Take it!'


@myapp.route('/read')
def read():
    return 'This is reading page'


@myapp.route('/read/text')
def text():
    return 'London is the capital of Great Britain!'


@myapp.route('/info')
def info():
    return 'My cool app'


if __name__ == '__main__':
    myapp.run(host='127.0.0.1', port=7777)
