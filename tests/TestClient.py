import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 6000
s.connect((host, port))
print("Connection established")

msg = s.recv(1024)
print(msg.decode("ascii"))
