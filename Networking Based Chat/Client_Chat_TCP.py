## Client program ##

# Importing the module
import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


host='127.0.0.1'        # Host ID
port=2303               # Port address
client.connect(('127.0.0.1',2303)) # Connecting client to server

print("Client Connected to Server...")

i=0
while i <= True:
    print("Server:","{}".format(client.recv(1023).decode('UTF-8')))     # printing The Server message
    msg=input("Client :")
    client.sendall(msg.encode('UTF-8'))

    
    


