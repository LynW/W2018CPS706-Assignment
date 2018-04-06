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
    MESSAGE = "Hello, World!"

    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "message:", MESSAGE

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

    data, addr = sock.recvfrom(1024)
    return str(data)


if __name__ == "__main__":
    app.run()
