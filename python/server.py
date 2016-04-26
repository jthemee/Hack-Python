#######################################
#@author - Jerome THEMEE
#@date - 26/04/2016
#@version - 1 - socket
#######################################

# import modules
import socket

# Constante 
ip_server = '10.3.108.131'                
port = 443   

# connection setting          
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind((ip_server, port))
socket_server.listen(10)
conn, addr = socket_server.accept()
print 'Connected by', addr

# connecting and send data
while 1:
    data = conn.recv(2048)
    print data
    if not data: break
    response = raw_input("shell> ")
    conn.sendall(response)
conn.close()

