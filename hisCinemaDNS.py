#hisCinemaDNS communicates with local_DNS with flags
import socket
import config


    '''
# --- Sending through UDP ---
# https://wiki.python.org/moin/UdpCommunication
UDP_IP = config.LOCAL_DNS_HOST
UDP_PORT = config.LOCAL_DNS_PORT
MESSAGE = "Grabbing"
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
print "Sending message to UDP IP:", UDP_IP,", UDP PORT:",UDP_PORT
# ----------------------------


# --- DNS AUTH ---
# --- https://wiki.python.org/moin/UdpCommunication
UDP_IP = config.LOCAL_DNS_HOST
UDP_PORT = 40041

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print "Received message:", data
    sock.close()
# -------------------------------------------------
    '''
    
UDP_IP = config.LOCAL_DNS_HOST #herCDN IP
UDP_PORT = config.LOCAL_DNS_PORT

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
sock.close()
