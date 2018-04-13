import socket
import config
import time
#receiving message from client asking for IP address of a video

udpip = config.LOCAL_DNS_HOST
udpport = config.LOCAL_DNS_PORT
buffersize = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udpip, udpport))

vidnum, addr = sock.recvfrom(buffersize)
print "Received request asking for video number: ",vidnum, "from address: ", addr

#SEARCHES DIRECTORY OF RECORDS FOR THAT RECORD FIND IP ADDRESS IS IN HISCINEMADNS
#I want to search each tuple in records.txt then split it into three parts (name, value, type) delimited by comma
# records are found in config.py
# IP and PORT aren't split
#for items in config.datafile:
  #if addr in items:
    #address =  (items[1]) # [1] ip address field in tuple
#print "Found", (address), "in", items

# uncomment below if PORT was included
'''
# split IP and PORT
for items in config.datafile:
  if addr in items:
    address =  (items[1]) # [1] ip address field in tuple
    splitter = (address.split(":"))
this_ip = splitter[0]
this_port = splitter[1]
print ("IP:",this_ip, "and PORT:", this_port)
    '''
    

print "Found video URL IP is in hisCinemaDNS in record: INSERT RECORD"

#forwards request to hiscinemaDNS
# Step 3: localDNS then request for video.hiscinema.com IP from hiscinemaDNS, (in hiscinemaDNS)hisCinemaDNS responds with herCDNDNS ip address NS type
udpport = 40044 #port using for connection with hiscinemaDNS
sock.sendto(vidnum,(udpip, udpport))
print "Sent request to hiscinemaDNS asking for video number: ",vidnum, "to address: ", udpip, ", ", udpport

data, addr = sock.recvfrom(buffersize)
print "Received message from hisCinemaDNS saying: ", data

# Step 4: localDNS contacts herCDNDNS for IP of video.hiscinema.com which herCDNDNS returns to localDNS
udpport = 40043 #port using for connection with herCDNDNS
sock.sendto(vidnum,(udpip, udpport))
print "Sent request to herCDNDNS asking for video number: ",vidnum, "to address: ", udpip, ", ", udpport

data, addr = sock.recvfrom(buffersize)
#PARSE RECORD RECEIVED HERE AND GET IP ADDRESS OF HERCDN.COM
ipher = "127.0.0.1,40042"
#tcpip,tcpport = str(data).split(':')
print "Received message from herCDNDNS with record, resolved IP for video number: ", vidnum

# Step 5: (in localDNS and client) localDNS then passes IP onto client
udpport = config.LOCAL_DNS_PORT
sock.sendto(ipher, (udpip, udpport))
print "Sent IP address of herCDN to client"



