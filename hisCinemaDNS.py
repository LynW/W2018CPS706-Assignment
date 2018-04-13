#hisCinemaDNS communicates with local_DNS with flags
import socket
import config

udpip = config.LOCAL_DNS_HOST
udpport = 40041 #port using for connection with hiscinemaDNS
buffersize = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udpip, udpport))

vidnum, addr = sock.recvfrom(buffersize)
print "Received request asking for video number: ",vidnum, "from address: ", addr

#SEARCHES DIRECTORY OF RECORDS FOR THAT VIDEO BUT REALIZES IT DOESN'T HAVE IT SO sends HERCDNDNS IP to localDNS
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

print "Found video URL IP is in herCDNDNS in record: INSERT RECORD"

#hisCinemaDNS responds with herCDNDNS ip address NS type
message = "go to herCDNDNS"
sock.sendto(message, (udpip, udpport))
print "Sent herCDNDNS IP to localDNS"
