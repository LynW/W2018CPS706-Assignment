#herCDNDNS only communicates with local_DNS

import socket
import config
import time

UDP_IP = config.herCinema_HOST
UDP_PORT = config.herCinema_PORT
MESSAGE = "{127.0.0.1,A}"


# --- https://wiki.python.org/moin/UdpCommunication
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print "received message:", data
    if not data: break
    sock.sendto(MESSAGE, addr)
    sock.close()



#I don't know how to check if this works
