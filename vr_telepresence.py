# vr_telepresence main

# imports
import time
from tcp_client import TcpClient
from sensor import Sensor
from stepper_mode import StepperMode
from stepper_driver import StepperDriver

# main function
def main():
	#tcpClientTest()
	stepperMotorTest()
	#readGyroscopeTest()

def readGyroscopeTest():
	gyroSensor = Sensor()
	while True:
		gyroData = gyroSensor.readGyroscope()


def stepperMotorTest():
	stepperMode = StepperMode(1, 2, 3)
	stepperMode.setResolution(1) # 1 is full step

	horizontalDriver = StepperDriver(11, 12)
	horizontalDriver.setDirection(1) # 1 is clockwise 0 is courterclockwise
	for x in range (0, 50):
		horizontalDriver.step()

def tcpClientTest():
	ipAddress = "192.168.1.107"
	port = 6000
	client = TcpClient(ipAddress, port)
	print("Trying to connect...")
	client.connect()
	print("Connected...")
	while True:
		message = client.read();
		if len(message) > 0:
			header = "Server: "
			print(header + message)
			
# call to main
main()
