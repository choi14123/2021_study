import socket
UDP_IP = '127.0.0.1'
UDP_PORT = 16002
MESSAGE = 'Hello, World! data!!! keyboard code skgjla'

print('UDP target IP:', UDP_IP)
print('UDP target port:', UDP_PORT)
print('message:', MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
				        socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
modifiedData = sock.recv(2048)
print('Received:', modifiedData)

sock.close()
