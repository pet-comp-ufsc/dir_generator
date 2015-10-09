from os import mkdir
from os.path import join
from uuid import uuid4

from flask import Flask
from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop

app = Flask(__name__)

BASE = '/seccom2015/user_homes'


@app.route('/get_home_dir', methods=['GET'])
def get_dir_name():
    dir_name = join(BASE, str(uuid4()))
    mkdir(dir_name)
    return dir_name


def run():
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5000)
    IOLoop.instance().start()


if __name__ == '__main__':
    run()
