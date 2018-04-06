import socket
import config
UDP_IP = config.LOCAL_DNS_HOST
UDP_PORT = config.LOCAL_DNS_PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data

    if data:
        print addr
        sock.sendto(b'This is the resolved IP address', addr)
