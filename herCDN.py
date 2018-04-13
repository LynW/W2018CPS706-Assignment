#herCDN sends the video to client

import socket
import config
import time

# --- Serve TCP --------------------
# https://wiki.python.org/moin/TcpCommunication
tcpip = config.herCinema_HOST
tcpport = config.herCinema_PORT
buffersize = 1024


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((tcpip, tcpport))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    data = conn.recv(BUFFER_SIZE)
    print "Received data from hisCinema asking for video number:", data

    if data == '1':
        fil = open('database/video1.mp4', 'rb')
    if data == '2':
        fil = open('database/video1.mp4', 'rb')
    if data == '3':
        fil = open('database/video1.mp4', 'rb')

        print "Opening file..."
        line = fil.read(1024)
        print "Reading file..."
        while (line):
            conn.send(line)
            line = fil.read(1024)
        print "Finished reading file"
        fil.close()
        conn.close()
        print "Closing connection."
sock.close()
# -----------------------------------
