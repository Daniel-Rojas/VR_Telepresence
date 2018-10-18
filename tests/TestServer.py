
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

serversocket.bind((host, port))
serversocket.listen(5)

print("Waiting for Connection...")
clientsocket, addr = serversocket.accept()
print ("Connected to %s" % str(addr))
msg = "Thank you for connecting"
clientsocket.send(msg.encode("ascii"))
clientsocket.close()


