# sensor class

# import
import board
import busio
import adafruit_lsm9ds1 as gyro

# class
class Sensor:

	def __init__(self):
		i2c = busio.I2C(board.SCL, board.SDA)
		self.sensor = gyro.LSM9DS1_I2C(i2c)
		print("Sensor: Created")

	def readGyroscope(self):
		gyroX, gyroY, gyroZ = self.sensor.gyro
		data = [gyroX, gyroY, gyroZ]
		return data

	def readAccelerometer(self):
		accelX, accelY, accelZ = self.sensor.acceleration
		data = [accelX, accelY, accelZ]
		return data

	def readMagnetometer(self):
		magX, magY, magZ = self.sensor.magnetic
		data = [magX, magY, magZ]
		return data

	def readTemperature(self):
		data = self.sensor.temperature
		return data