import os
import sys
from wsgiref.simple_server import make_server

def app(environ, start_response):
    status = '404 Not Found'
    response_headers = [("Content-Type", "text/html")]
    result = ['File not found!']
    
    if environ["PATH_INFO"] == "/" or environ["PATH_INFO"] == "/index.html":
        file = open('./index.html', 'rb')
        result = []       
        for line in file:
            result.append(line)
        file.close()
        status = '200 OK'


    elif environ["PATH_INFO"] == "/about/aboutme.html":
        file = open('./about/aboutme.html', 'rb')
        result = []
        for line in file:
            result.append(line)
        file.close()
        status = '200 OK'

    start_response(status, response_headers)
    return result

class Middleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        top_str = "<div class='top'>Middleware TOP</div>\n"
        bottom_str = "<div class='bottom'>Middleware BOTTOM</div>\n"
        body_open = "<body>"
        body_close = "</body>"

        for line in self.app(environ, start_response):
            if line.find(body_open) != -1:
                yield line
                yield top_str
            elif line.find(body_close) != -1:
                yield bottom_str
                yield line
            else:
                yield line

app = Middleware(app)
if __name__ == '__main__':
    _server = make_server('localhost', 8000, app)
    print "Serving localhost on port 8000..."
    _server.serve_forever()







