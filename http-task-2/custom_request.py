import socket

_socket = socket.socket()
_socket.connect(('httpbin.org',80))
_socket.send("""POST /post HTTP/1.1
Host: httpbin.org
Content-Type: application/json
Content-Length: 80
Accept: */*

{
    "github": "ragozin-n",
    "Name": "Nikita",
    "Surname": "Ragozin"
}\n\n
""")

_responce = _socket.recv(1024)
print(_responce)

_socket.close()