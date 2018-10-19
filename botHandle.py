#!/usr/bin/python2.7

import sys,os
import time
import telepot
import RPi.GPIO as GPIO

PIN_LAMP1 = 18
PIN_LAMP2 = 23
PIN_LAMP3 = 24
PIN_LAMP4 = 25
# Config of GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LAMP1,GPIO.OUT)
GPIO.setup(PIN_LAMP2,GPIO.OUT)
GPIO.setup(PIN_LAMP3,GPIO.OUT)
GPIO.setup(PIN_LAMP4,GPIO.OUT)

def Help():
	return """
		Hi , 
		How to use: =)
			Lamp1 On 	: Lamp 1 ON
			Lamp1 OFF 	: Lamp 1 OFF
			Lamp2 On 	: Lamp 2 ON
			Lamp2 OFF 	: Lamp 2 OFF
			Lamp3 On 	: Lamp 3 ON
			Lamp3 OFF 	: Lamp 3 OFF
			Lamp4 On 	: Lamp 4 ON
			Lamp4 OFF 	: Lamp 4 OFF
	"""

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
		if msg['text'].lower() == "lamp1 off":
				GPIO.output(PIN_LAMP1,False)
			    bot.sendMessage(chat_id, "LAMP 1 is OFF") #msg['text'])
		elif msg['text'].lower() == "lamp1 on":
				GPIO.output(PIN_LAMP1,True)
			    bot.sendMessage(chat_id, "LAMP 1 is ON") #msg['text'])
		elif msg['text'].lower() == "lamp2 off":
				GPIO.output(PIN_LAMP2,False)
			    bot.sendMessage(chat_id, "LAMP 2 is OFF") #msg['text'])
		elif msg['text'].lower() == "lamp2 on":
				GPIO.output(PIN_LAMP2,True)
			    bot.sendMessage(chat_id, "LAMP 2 is ON") #msg['text'])
		elif msg['text'].lower() == "lamp3 off":
				GPIO.output(PIN_LAMP3,False)
			    bot.sendMessage(chat_id, "LAMP 3 is OFF") #msg['text'])
		elif msg['text'].lower() == "lamp3 on":
				GPIO.output(PIN_LAMP3,True)
			    bot.sendMessage(chat_id, "LAMP 3 is ON") #msg['text'])
		elif msg['text'].lower() == "lamp4 off":
				GPIO.output(PIN_LAMP4,False)
			    bot.sendMessage(chat_id, "LAMP 4 is OFF") #msg['text'])
		elif msg['text'].lower() == "lamp4 on":
				GPIO.output(PIN_LAMP4,True)
			    bot.sendMessage(chat_id, "LAMP 4 is ON") #msg['text'])
		else:
			    bot.sendMessage(chat_id, Help())#"Your Command Not found namOsan! =)") #msg['text'])
	#print msg['text']

#TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot("388734844:AAGaAAAx_4K-276pvAd87SpB3O8ogUZke4I")
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
