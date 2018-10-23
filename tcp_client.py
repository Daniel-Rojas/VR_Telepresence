# tcp client class

# imports
import socket as Socket

# class definition
class TcpClient:

	def __init__(self, ipAddress, port):
		self.ipAddress = ipAddress
		self.port = port
		self.socket = Socket.socket(Socket.AF_INET, Socket.SOCK_STREAM)

	def connect(self):
		self.socket.connect((self.ipAddress, self.port))
		print("Connection Established...")

	def read(self):
		recievedMessage = self.socket.recv(1024)
		decodedMessage = recievedMessage.decode("ascii")
		return decodedMessage

	def write(self, message):
		self.socket.send(message)



