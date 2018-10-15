import socket


TCP_IP = '221.132.29.148'
TCP_PORT = 3003
BUFFER_SIZE = 1024
MESSAGE = "python PC Le Dai Hanh"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.sendall(MESSAGE.encode('utf-8'))
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:"), data