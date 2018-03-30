import RPi.GPIO as GPIO
import time

class Buzzer:

    def __init__(self, pin, delay):
        self.pin = pin
        self.delay = delay
        self.status = "ON"

    def stop(self):
        self.status = "OFF"
        
    def setDelay(self, delay):
        self.delay = delay

    def on(self):
        GPIO.output(self.pin, True)

    def off(self):
        GPIO.output(self.pin, False)

    def blink(self):
        self.on()
        time.sleep(float(self.delay)/2.0)
        self.off()
        time.sleep(float(self.delay))
