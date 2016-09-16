import socket

_requests = [
"""GET /ip HTTP/1.1
Host: httpbin.org
Accept: */*
Connection: close\n\n""",
"""GET /get?foo=bar&1=2&2/0&error=True HTTP/1.1
Host: httpbin.org
Accept: */*
Connection: close\n\n""",
"""POST /post HTTP/1.1
Host: httpbin.org
Accept: */*
Content-Length: 35
Content-Type: application/x-www-form-urlencoded\n
foo=bar&1=2&2%2F0=&error=True
Connection: close\n\n""",
"""GET /cookies/set?country=Ru HTTP/1.1
Host: httpbin.org
Accept: */*
Connection: close\n\n""",
"""GET /cookies HTTP/1.1
Host: httpbin.org
Accept: */*
Connection: close\n\n""",
"""GET /redirect/4 HTTP/1.1
Host: httpbin.org
Accept: */*
Connection: close\n\n"""]

for item in _requests:
    print("Request:" + item)
    _socket = socket.socket() 
    _socket.connect(("httpbin.org", 80)) 
    _socket.send(item) 
    _data = _socket.recv(1024)
    _socket.close()
    print ("\nResponce: " + _data + "\n----------------------\n")