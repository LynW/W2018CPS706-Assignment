import config
import socket 

#tcp connection established with client to sen index file
tcpip = config.hisCinema_HOST
tcpport = config.hisCinema_PORT
buffersize = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((tcpip,tcpport))
sock.listen(1)

while True:

	conn, addr = sock.accept()
	data = conn.recv(buffersize)
	print "Message received from address: ",addr,"saying: ",data

	if data:
		print "Opening index.html..."
		fil = open('templates/index.html', 'rb')

		print "Reading index.html..."
		line = fil.read(1024)
		while (line):
			conn.send(line)
			line = fil.read(1024)

		print "index.html sent."

		fil.close()
		conn.close()
		print "Connection Closed"