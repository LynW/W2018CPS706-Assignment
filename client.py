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
	
	data, addr = sock.recvfrom(1024) #Getting data
	ip,port = str(data).split(',')
	message = str(num) #This message will be sent to herCDN
    #have video variable with 1,2, or 3 and that gets evaluated when looking to see which video file to send? 

	# Step 6: client establishes TCP connection with herCDN and requests video number: 1
	tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcpsock.connect((ip, int(port)))
	print "Connecting to TCP PORT:", ip, ", TCP PORT:", int(port)

	tcpsock.send(message)
	print "Sending message to herCDN asking for video number: .", num, "to be sent." 

	#waiting for file 
	fil = open('client/downloaded',num,".mp4", 'wb')
	print "Opening file to store video in client..."

	data = tcpsock.recv(BUFFER_SIZE)
	print "Receiving video file..."
	#print "data is: " + data

	while(data):
		fil.write(data)
		data = tcpsock.recv(BUFFER_SIZE)
	fil.close()
	print "Done downloading."
	return render_template('complete.html')
	#return str('DOWNLOADING complete') #Page loads this when done receiving file
	data = tcpsock.recv(BUFFER_SIZE)
	tcpsock.close()
	print "Closing socket."
	return str(data)

if __name__ == "__main__":
    app.run()


# Step 3: (in localDNS) localDNS then request for video.hiscinema.com IP from hiscinemaDNS, hisCinemaDNS responds with herCDNDNS ip address NS type
# Step 4: (in localDNS) localDNS contacts herCDNDNS for IP of video.hiscinema.com which herCDNDNS returns to localDNS
# Step 5: (in localDNS and client) localDNS then passes IP onto client 
# Step 6: client establishes TCP connection with herCDN and requests video number: 1
# Step 7: hercinema receives request and sends video file over TCP, which downloads onto client and then plays. 