import RPi.GPIO as GPIO
import time
sensor0=20
sensor1=21
sensor2=16
red_led=26
green_led=19
# sensor1=22
# sensor2=23
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(sensor0,GPIO.IN)
GPIO.setup(sensor1,GPIO.IN)
GPIO.setup(sensor2,GPIO.IN)
GPIO.setup(green_led,GPIO.OUT)
GPIO.setup(red_led,GPIO.OUT)

# RPi.GPIO.setup(sensor1,RPi.GPIO.IN)
# RPi.GPIO.setup(sensor2,RPi.GPIO.IN)
while True:
    if(((GPIO.input(sensor2))&(GPIO.input(sensor0))&(GPIO.input(sensor1)))==True):
#     if(GPIO.input(sensor2)==True):
        GPIO.output(green_led,GPIO.LOW)
        GPIO.output(red_led,GPIO.HIGH)
    else:
        GPIO.output(red_led,GPIO.LOW)
        GPIO.output(green_led,GPIO.HIGH)
    time.sleep(1)
    