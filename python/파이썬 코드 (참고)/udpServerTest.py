import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 16002

sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print('Connected by', addr)
    modifiedData = data.decode().upper()
    print ('received message:', data)
    sock.sendto(modifiedData.encode(), addr)


 

