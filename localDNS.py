import socket
import config 

#receiving message from client asking for IP address of a video

udpip = config.LOCAL_DNS_HOST
udpport = config.LOCAL_DNS_PORT
buffersize = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udpip, udpport))

vidnum, addr = sock.recvfrom(buffersize) 
print "Received request asking for video number: ",vidnum, "from address: ", addr

#SEARCHES DIRECTORY OF RECORDS FOR THAT RECORD FIND IP ADDRESS IS IN HISCINEMADNS
print "Found video URL IP is in hisCinemaDNS in record: INSERT RECORD"

#forwards request to hiscinemaDNS
# Step 3: localDNS then request for video.hiscinema.com IP from hiscinemaDNS, (in hiscinemaDNS)hisCinemaDNS responds with herCDNDNS ip address NS type
udpport = 40041 #port using for connection with hiscinemaDNS
sock.sendto(vidnum,(udpip, udpport))
print "Sent request asking for video number: ",vidnum, "to address: ", udpip, ", ", udpport

data, addr = sock.recv(buffersize)
print "Received message from hisCinemaDNS saying: ", data

# Step 4: localDNS contacts herCDNDNS for IP of video.hiscinema.com which herCDNDNS returns to localDNS
udpport = 40042 #port using for connection with herCDNDNS
sock.sendto(vidnum,(udpip, udpport))
print "Sent request asking for video number: ",vidnum, "to address: ", udpip, ", ", udpport

data, addr = sock.recv(buffersize)
tcpip,tcpport = str(data).split(':')
print "Received message from herCDNDNS with record, resolved IP for video number: ", vidnum

# Step 5: (in localDNS and client) localDNS then passes IP onto client 

