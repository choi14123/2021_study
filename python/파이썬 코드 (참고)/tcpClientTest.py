import socket
 
HOST = '127.0.0.1'                # The remote host
PORT = 16001              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(('Hello, world New world').encode())
data = s.recv(1024)
s.close()
print ('Received', data.decode())
