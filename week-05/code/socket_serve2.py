#!/usr/bin/env python

"""
Example from the HowTo:

http://docs.python.org/howto/sockets.html

Then edited by Chris Barker
"""

HOST = "localhost"
PORT = 55555

import socket

#create an INET, STREAMing socket
serversocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#bind the socket to localhost, high port
serversocket.bind((HOST, PORT),)
#become a server socket
serversocket.listen(5)

html = """
<html>
    <body>
        <h1>This is some text.</h1>
    </body>
</html>"""


# accept a single request
#while True:
if True:
    #accept connections from outside
    print "calling accept"
    (clientsocket, address) = serversocket.accept()
    print "accept returned"
    #now do something with the clientsocket
    #in this case, we'll pretend this is a threaded server
    #ct = client_thread(clientsocket)
    #ct.run()
    print "got something:", clientsocket
    print "from address", address
    print clientsocket.recv(1024)
    
    # now lets send something:
    clientsocket.send(html)
    
## put this in your browser while this is running:
##    http://localhost:55555/a_file