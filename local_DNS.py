# local_DNS communicates with
#1. Client 
#2. hisCinemaDNS
#3. herCinemaDNS


import socket
import config
import time

UDP_IP = config.LOCAL_DNS_HOST
UDP_PORT = config.LOCAL_DNS_PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))


# --- Receiving file transfers Through UDP ----------
while True:
    data, address = sock.recvfrom(1024)
    print "local_DNS received message:", data

    if data:
        print "Data was given at this address: ",address
        print "Resolved the DNS query"
        sock.sendto(b'127.0.0.1:40049', address) #TCP_PORT
# --------------------------------------------------
