from flask import Flask
from flask import render_template
import config
import socket

app = Flask(__name__)

#The default URL to go to:
@app.route('/')
def hello_world():
    return "Local DNS Port:"
    return str(config.LOCAL_DNS_PORT)



@app.route('/hello/')
def hello():
    return render_template('index.html')



@app.route('/hello2/')
def hello2():

    UDP_IP = config.LOCAL_DNS_HOST
    UDP_PORT = config.LOCAL_DNS_PORT
    MESSAGE = "Grabbing"

    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "message:", MESSAGE

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

    data, addr = sock.recvfrom(1024) #Getting data

    ip,port = str(data).split(':')

    #Connecting to database through TCP connection
    #TCP_IP = '127.0.0.1'
    #TCP_PORT = 5005
    BUFFER_SIZE = 1024
    MESSAGE = "Please send me video file 1"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, int(port)))
    s.send(MESSAGE)

    f = open('client/downloaded1.mp4', 'wb')
    data = s.recv(BUFFER_SIZE)

    n = 1
    while(data):
        print "Receiving...", n+1
        f.write(data)
        data = s.recv(BUFFER_SIZE)
    f.close()
    return str('DOWNLOADING complete')


    data = s.recv(BUFFER_SIZE)
    s.close()
    return str(data)

if __name__ == "__main__":
    app.run()
