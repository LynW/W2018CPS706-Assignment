#herCDN sends the video to client

import socket
import config


# --- Serve TCP --------------------
# https://wiki.python.org/moin/TcpCommunication
TCP_IP = '127.0.0.1'
TCP_PORT = 40049
BUFFER_SIZE = 1024


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    data = conn.recv(BUFFER_SIZE)
    print "Received data from hisCinema containing message:", data

    if data:
        f = open('database/video1.mp4', 'rb')
        print "Opening file."
        l = f.read(1024)
        print "Starting to read."
        while (l):
            conn.send(l)
            l = f.read(1024)
        print "Finished reading."
        f.close()
        conn.close()
        print "Closing connection."
# -----------------------------------
