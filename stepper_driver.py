# stepper driver class

# imports
import time
import GPIO as gpio

# class
class StepperDriver:

	def __init__(self, stepPin, dirPin):
		self.stepPin = stepPin
		self.dirPin = dirPin

	def setupPins(self):
		gpio.setmode(gpio.BCM)
		gpio.setup(self.stepPin, gpio.OUT)
		gpio.setup(self.dirPin, gpio.OUT)

	def setDirection(self, direction):
		gpio.output(self.dirPin, direction)

	def step(self):
		gpio.output(self.step, 1)
		time.sleep(0.001)
		gpio.output(self.step, 0)
		time.sleep(0.001)
