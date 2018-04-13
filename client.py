# Client receives data from herCDN
# Communicates with hisCinema
# 2 on the diagram (IDK what that does)
#questions: 
	#when to use V or R flag?
# Step 1: client to do all the opening, gets everything, tcp conenction with hiscinema sends index file, client displays it 
import socket
import config
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
	# https://wiki.python.org/moin/TcpCommunication
	tcpip = config.hisCinema_HOST
	tcpport = config.hisCinema_PORT
	buffersize = 1024
	message = "Send hiscinema.com html file with video links"

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((tcpip, tcpport));
	sock.send(message)
	print"Client requests videos.hiscinema.com from www.hiscinema.com web server at IP address: ",tcpip," and port: ",tcpport

	#hiscinema receives this request and sends over index.html
	data = sock.recv(buffersize)
	print "Receiving index.html..."

	fil = open('templates/vid.html', 'wb')
	print "Opening file to write index.html into..."

	while(data):
	    fil.write(data)
	    data = sock.recv(buffersize)
	fil.close()
	print "Writing into vid.html..."
	return render_template('vid.html')
	sock.close()
	print "Connection closed."
	#displays index.html file on browser
	return str(data)

# Step 2: when video is clicked to be downloaded, request sent to localDNS for IP address of video.hiscinema.com/v1 which is in hiscinemaDNS
@app.route('/video/<string:num>/')
def vid(num):
	print "Video number: ", num, "clicked."
	udpip = config.LOCAL_DNS_HOST
	udpport = config.LOCAL_DNS_PORT
	message = str(num)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(message, (udpip, udpport))
	print "Requesting IP address for video/",num, "/ from localDNS at UDP IP: ",udpip," and UDP PORT: ",udpport
	
	return

if __name__ == "__main__":
    app.run()


# Step 3: (in localDNS) localDNS then request for video.hiscinema.com IP from hiscinemaDNS, hisCinemaDNS responds with herCDNDNS ip address NS type
# Step 4: (in localDNS) localDNS contacts herCDNDNS for IP of video.hiscinema.com which herCDNDNS returns to localDNS
# Step 5: localDNS then passes IP onto client 
# Step 6: client establishes TCP connection with herCDN and requests video number: 1
# Step 7: hercinema receives request and sends video file over TCP, which downloads onto client and then plays. 