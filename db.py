#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 8000
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    data = conn.recv(BUFFER_SIZE)
    print "Received data:", data
    if not data:
        f = open('database/video1.mp4', 'rb')
        l = f.read(1024)
        while (l):
            conn.send(1)
            l = f.read(1024)
        f.close()
        
conn.close()
