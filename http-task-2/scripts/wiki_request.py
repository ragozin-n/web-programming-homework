import socket

_socket = socket.socket()
_socket.connect(('wikipedia.org',80))
_socket.send(
"""GET /wiki/Lake_Chaubunagungamaug HTTP/1.1
Host: wikipedia.org
User-Agent: Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008050509
Firefox/3.0b5
Accept: text/html
Connection: close\n\n
""")

_buffer = _socket.recv(1024)
_data = ""
while _buffer:
    _data += _buffer
    _buffer = _socket.recv(1024)
_socket.close()
print(_data)