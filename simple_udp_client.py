import socket

#get target
target_host = input('[?] Taget URL/IP: ')
#this loop keeps asking for a port until a valid one is supplied
target_port = None
while target_port == None:
	try:
		target_port = int(input('[?] Target port: '))
	except: 
		print('Enter a valid port!')

#create a socket object  
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data
client.sendto(b"ABC",(target_host,target_port))

#receive some data and a return address
data, addr = client.recvfrom(4096)

print(data.decode(),addr)
client.close()