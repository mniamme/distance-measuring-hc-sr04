"""This is a class for handling HC-RS04 sensor functions"""
import RPi.GPIO as GPIO
import time

class HCRS:
    
    def __init__(self, TRIG, ECHO, delay):
        self.TRIG = TRIG
        self.ECHO = ECHO
        self.delay = delay
            
    def read(self):
        """This method will read one reading from the sensor"""
        TRIG = self.TRIG
        ECHO = self.ECHO
        delay = self.delay
        # settling the sensor
        GPIO.output(TRIG, False)
        time.sleep(delay)

        # send a signal
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        #catch a signal
        error = 0
        while GPIO.input(ECHO) == 0:
            start_time = time.time()
            error += 1
            if error > 1000:
                break
        if error > 1000:
            return -1
        
        
        while GPIO.input(ECHO) == 1:
            end_time = time.time()

        # calculate the distance 
        total_time = end_time - start_time

        distance = (34300 * total_time) / 2

        distance = round(distance, 2)

        return distance
        
