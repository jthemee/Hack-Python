import socket,os
# target
target_host = "127.0.0.1"
target_port = 8080

# create the socket object with python
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server on 8080
client.connect((target_host,target_port))

 # send some data to the server
#request = "connected with me" 
#client.send(request)
 
 # receive data from google
#response = client.recv(4096)

 # print the response 
files = str(os.listdir("."))
client.send(files)
