from hcrs import HCRS
from led import LED
from buzzer import Buzzer
import RPi.GPIO as GPIO
import time
import thread

# setup
GPIO.setmode(GPIO.BOARD)

BUZZER = 12
TRIG = 16
ECHO = 18
WARNINGLED = 38
DANGERLED = 40

GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.IN)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

# initialize components
sensor = HCRS(TRIG, ECHO, 2)
warningLed = LED(WARNINGLED)
dangerLed = LED(DANGERLED)
buzz = Buzzer(BUZZER, 1)

# start all
def buzzing(buzz):
    while buzz.status == "ON":
        buzz.blink()
    else:
        return

try:
    thread.start_new_thread(buzzing, (buzz, ))
    while True:
        distance = sensor.read()
        if distance == -1:
            print "Distance Is Out Of Range"
            warningLed.off()
            dangerLed.off()
        else:
            buzz.setDelay(float(distance * 0.03)) 
            if distance <=22 and distance >= 12:
                warningLed.on()
                dangerLed.off()
            elif distance < 12:
                warningLed.off()
                dangerLed.on()
            else:
                warningLed.off()
                dangerLed.off()
            print "Distance:", distance, "cm"

except Exception:
    buzz.stop()
    warningLed.off()
    dangerLed.off()
    GPIO.cleanup()
except KeyboardInterrupt:
    buzz.stop()
    warningLed.off()
    dangerLed.off()
    GPIO.cleanup()
