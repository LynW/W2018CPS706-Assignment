import socket
import config
import time

UDP_IP = config.LOCAL_DNS_HOST
UDP_PORT = config.LOCAL_DNS_PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))



while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "Local_DNS Received message:", data

    if data:
        print "I got a data from this address: ",addr
        print "Resolve the DNS query"
        print "It is done the 127.0.0.1:8000 give back to the client"
        sock.sendto(b'127.0.0.1:8000', addr)
