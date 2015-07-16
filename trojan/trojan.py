import socket
import threading

bind_ip = "0.0.0.0" # local IP
bind_port = 8080    # port that you're locking for

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating object
server.bind((bind_ip,bind_port))  #bind called 
server.listen(5)  # 5 connections possible

print "[*] listening on %s:%d" %(bind_ip,bind_port) # say hi !

# client handle thread
def handle_client(client_socket):
	#print the client data
	request = client_socket.recv(2048)
	
	print "[*] Received: %s" % request
	#send back the packet 
	response = raw_input("which command command would you like to send ?\n")
	client_socket.send(response)
	client_socket.close()

while True: #loop for waiting connections
	client,addr = server.accept()
	print "[*] Accepted connection from %s:%d" % (addr[0],addr[1])
# threading started
	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()
