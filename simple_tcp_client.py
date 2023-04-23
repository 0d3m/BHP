import socket

#get target
target_host = 'localhost'
#this loop keeps asking for a port until a valid one is supplied
target_port = 9998
while target_port == None:
	try:
		target_port = int(input('[?] Target port: '))
	except: 
		print('Enter a valid port!')

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect client to target
client.connect((target_host, target_port))

#send some data as bytes
client.send(b"SUGONMA DEEEK")

#save the data received from target to a variable
response = client.recv(420)

print(response.decode())

#close connection to target
client.close()

