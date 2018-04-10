# PREVIOIUSLY website.py

from flask import Flask
from flask import render_template
import config
import socket

app = Flask(__name__)

#The default URL to go to:
@app.route('/')
def hello():
    return render_template('index.html')
    print "Local DNS Port: " + str(config.LOCAL_DNS_PORT)



@app.route('/video/<string:n>/')
def download(num):
    return  "download"


#We can do this the super inefficient way.
@app.route('/video1/')
def hello2():

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

    data, addr = sock.recvfrom(1024) #Getting data
    ip,port = str(data).split(':')

    # --- Connecting to database through TCP connection ---
    # https://wiki.python.org/moin/TcpCommunication
    BUFFER_SIZE = 1024
    MESSAGE = "Please send me video file" #This message will be sent to herCDN

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, int(port)))
    print "Connecting to TCP PORT:", ip, ", TCP PORT:", int(port)

    s.send(MESSAGE)
    print "Sending message to herCDN."

    f = open('client/downloaded1.mp4', 'wb')
    print "Opening file..."

    data = s.recv(BUFFER_SIZE)
    print "Receiving..."

    while(data):
        f.write(data)
        data = s.recv(BUFFER_SIZE)
    f.close()
    print "Done downloading."
    return str('DOWNLOADING complete') #Page loads this when done receiving file
    data = s.recv(BUFFER_SIZE)
    s.close()
    print "Closing socket."
    return str(data)
    # ------------------------------------------------------


if __name__ == "__main__":
    app.run()
