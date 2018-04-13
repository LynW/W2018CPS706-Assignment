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
print "Found video URL IP is in herCDNDNS in record: INSERT RECORD"

#hisCinemaDNS responds with herCDNDNS ip address NS type
message = "go to herCDNDNS"
sock.sendto(message, (udpip, udpport))
print "Sent herCDNDNS IP to localDNS"

