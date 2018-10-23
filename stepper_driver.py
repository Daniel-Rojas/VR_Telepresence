# stepper driver class

# imports
import time
import GPIO as gpio

# class
class StepperDriver:

	def __init__(self, stepPin, dirPin):
		self.stepPin = stepPin
		self.dirPin = dirPin
		print("StepperDriver: Created")
		self.setupPins()

	def setupPins(self):
		gpio.setmode(gpio.BCM)
		gpio.setup(self.stepPin, gpio.OUT)
		gpio.setup(self.dirPin, gpio.OUT)
		# default to clockwise direction
		gpio.output(self.dirPin, 1)
		print("StepperDriver: Setup Complete")

	def setDirection(self, direction):
		if direction == 0 || direction == 1:
			gpio.output(self.dirPin, direction)
			print("StepperDriver: Direction Set")
		else
			print("StepperDriver: ERROR Invalid Direction")

	def step(self):
		gpio.output(self.stepPin, 1)
		time.sleep(0.001)
		gpio.output(self.stepPin, 0)
		time.sleep(0.001)
		print("StepperDriver: Step")
