# vr_telepresence main

# imports
from tcp_client import TcpClient

# main function
def main():
	ipAddress = "192.168.1.107"
	port = 6000
	client = TcpClient(ipAddress, port)
	client.connect()
	while True:
		message = client.read();
		if len(message) > 0:
			print(message)
			
# call to main
main()
