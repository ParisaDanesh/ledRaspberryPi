import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
PIN_LAMP1 = 18
PIN_LAMP2 = 23
PIN_LAMP3 = 24
PIN_LAMP4 = 25
GPIO.setup(PIN_LAMP1,GPIO.OUT)
GPIO.setup(PIN_LAMP2,GPIO.OUT)
GPIO.setup(PIN_LAMP3,GPIO.OUT)
GPIO.setup(PIN_LAMP4,GPIO.OUT)

while True:
	GPIO.output(PIN_LAMP2,True)
	print "LED on"
	time.sleep(1)
	GPIO.output(PIN_LAMP2,False)
	print "LED off"
	time.sleep(1)
