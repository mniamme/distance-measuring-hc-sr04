import RPi.GPIO as GPIO
import time

class LED:

    def __init__(self, pin):
        self.pin = pin
        
    def on(self):
        GPIO.output(self.pin, True)

    def off(self):
        GPIO.output(self.pin, False)
