'''
Created By   : NAVEEN RAJU.K
Craeted date : 12th JUNE 2021
info         : Python program for network based chat application.
'''
## Server program ## 

# Importing  the module 
import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #Creating the Object


host='127.0.0.1'    # Host ID
port=2303           # Port address

server.bind(('127.0.0.1',2303))     # connecting client

server.listen()

print("Server waiting for Client to connect...")

while True:
    data,addrs=server.accept()
    i=0
    while i <= True:
        msg=input("Server Enter your message:")   #Getting message from the Server
        data.sendall(msg.encode('UTF-8'))
        print("Client:",'{}'.format(data.recv(1023).decode('UTF-8')))       # Printing the client message
        
        
