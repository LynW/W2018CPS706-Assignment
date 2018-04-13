# Client receives data from herCDN
# Communicates with hisCinema
# 2 on the diagram (IDK what that does)
#questions: 
	#when to use V or R flag?
# Step 1: client to do all the opening, gets everything, tcp conenction with hiscinema sends index file, client displays it 
import socket
import config

# https://wiki.python.org/moin/TcpCommunication
tcpip = config.hisCinema_Host
tcpport = config.hisCinema_PORT
buffersize = 1024
message = "Send hiscinema.com html file with video links"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(tcpip, tcpport);
sock.send(message)
print"Client requests videos.hiscinema.com from www.hiscinema.com web server at IP address: " + tcpip + " and port: " + tcpport

#hiscinema receives this request and sends over index.html

(name, value, type)
(video.hiscinema.com, hiscinemaDNS, NS)
(name, value, V - video)
(name, value, R - redirect)

# Step 2: when video is clicked to be downloaded, request sent to localDNS for IP address of video.hiscinema.com/v1 which is in hiscinemaDNS
# Step 3: localDNS then request for video.hiscinema.com IP from hiscinemaDNS, hisCinemaDNS responds with herCDNDNS ip address NS type
# Step 4: localDNS contacts herCDNDNS for IP of video.hiscinema.com which herCDNDNS returns to localDNS
# Step 5: localDNS then passes IP onto client 
# Step 6: client establishes TCP connection with herCDN and requests video number: 1
# Step 7: hercinema receives request and sends video file over TCP, which downloads onto client and then plays. 