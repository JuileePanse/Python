#!/usr/bin/python

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
string_value = s.recv(1024)
print ('\n > ' + string_value)
s.send('I miss you.')
print('\n > ' + s.recv(1024))
s.send('I met a very nice girl (or guy). I am wondering whether my allowance can be increased?')
print('\n > ' + s.recv(1024))
s.close()                   # Close the socket when done