#herCDNDNS only communicates with local_DNS

import socket
import config

udpip = config.LOCAL_DNS_HOST
udpport = 40042 #port using for connection with herCDNDNS
buffersize = 1024

#FORMAT OF RECORDS >>>>>>>> MESSAGE = "{127.0.0.1,A}"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udpip, udpport))

vidnum, addr = sock.recvfrom(buffersize) 
print "Received request asking for video number: ",vidnum, "from address: ", addr

#SEARCHES DIRECTORY OF RECORDS FOR THAT VIDEO, FINDS IT AND SENDS IT TO LOCALDNS
print "Found record: INSERT RECORD"
record = str(configure.herCinema_HOST:configure.herCinema_PORT)
#herCDNDNS responds with record A type
sock.sendto(record, (udpip, udpport))
print "Sent record to localDNS"
