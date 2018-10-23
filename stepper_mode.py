# stepper mode class

# imports
import RPi.GPIO as gpio

# class
class StepperMode:

	def __init__(self, pin0, pin1, pin2):
		self.pin0 = pin0
		self.pin1 = pin1
		self.pin2 = pin2
		print("StepperMode: Created")
		self.setupPins()

	def setupPins(self):
		gpio.setmode(gpio.BCM)
		gpio.setup(self.pin0, gpio.OUT)
		gpio.setup(self.pin1, gpio.OUT)
		gpio.setup(self.pin2, gpio.OUT)
		# default to full step resolution
		gpio.output(self.pin0, 0)
		gpio.output(self.pin0, 0)
		gpio.output(self.pin0, 0)		
		print("StepperMode: Setup Complete")

	def setResolution(self, resolution):
		if resolution == 1:
			gpio.output(self.pin0, 0)
			gpio.output(self.pin0, 0)
			gpio.output(self.pin0, 0)
		elif resolution == 2:
			gpio.output(self.pin0, 0)
			gpio.output(self.pin0, 0)
			gpio.output(self.pin0, 1)
		elif resolution == 4:
			gpio.output(self.pin0, 0)
			gpio.output(self.pin0, 1)
			gpio.output(self.pin0, 0)
		elif resolution == 8:
			gpio.output(self.pin0, 0)
			gpio.output(self.pin0, 1)
			gpio.output(self.pin0, 1)
		elif resolution == 16:
			gpio.output(self.pin0, 1)
			gpio.output(self.pin0, 0)
			gpio.output(self.pin0, 0)
		elif resolution == 32:
			gpio.output(self.pin0, 1)
			gpio.output(self.pin0, 0)
			gpio.output(self.pin0, 1)
		else:
			gpio.output(self.pin0, 0)
			gpio.output(self.pin0, 0)
			gpio.output(self.pin0, 0)

		print("StepperMode: Resolution Set")			

