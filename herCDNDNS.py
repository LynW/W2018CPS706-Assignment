#herCDNDNS only communicates with local_DNS

import socket
import config
import re

udpip = config.LOCAL_DNS_HOST
udpport = 40042 #port using for connection with herCDNDNS
buffersize = 1024

#FORMAT OF RECORDS >>>>>>>> MESSAGE = "{127.0.0.1,A}"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udpip, udpport))

vidnum, addr = sock.recvfrom(buffersize)
print "Received request asking for video number: ",vidnum, "from address: ", addr

#SEARCHES DIRECTORY OF RECORDS FOR THAT VIDEO, FINDS IT AND SENDS IT TO LOCALDNS
#I want to search each tuple in records.txt then split it into three parts (name, value, type) delimited by comma
# records are found in config.py
# IP and PORT aren't split
for items in config.datafile:
  if addr in items:
    address =  (items[1]) # [1] ip address field in tuple
print "Found", (address), "in", items

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

print "Found record:"

# Should this be: record = str(this_ip:this_port) ?
record = "The record containing that video is in here"
#herCDNDNS responds with record A type
sock.sendto(record, (udpip, udpport))
print "Sent record to localDNS"
