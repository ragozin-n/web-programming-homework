import os
import socket

_socket = socket.socket()
_socket.bind(('localhost',8080))
_socket.listen(1)
print ('Serving on ' + str(HOST) + ':' + str(PORT))

while True:
	connection, _address = _socket.accept()
	data = connection.recv(1024)
	request = data.decode("utf-8").split("\r\n", 1)[0]
	address = request.split(" ")[1]
	
	if address == "/index.html" or address == "/":
		if os.path.exists("./index.html"):
			file = open ("./index.html", "rb")
			connection.send("""HTTP/1.1 200 OK \n Content type:text HTML\n\n\n """ + file.read())
			file.close()

	elif address == "/about/aboutme.html":
		if os.path.exists("." + address):
			file = open ("." + address, "rb")
			connection.send("""HTTP/1.1 200 OK \n Content type:text HTML\n\n\n """ + file.read())	
			file.close()
	connection.close()
_socket.close()