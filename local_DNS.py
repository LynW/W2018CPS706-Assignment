import socket
import config
import time

UDP_IP = config.LOCAL_DNS_HOST
UDP_PORT = config.LOCAL_DNS_PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))


# --- Receiving file transfers Through UDP ----------
while True:
    data, address = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "Local_DNS received message:", data

    if data:
        print "Data was given at this address: ",address
        print "Resolved the DNS query"
        print "Success, ", address, "video has been sent to client."
        sock.sendto(b'127.0.0.1:8000', address)
# --------------------------------------------------
