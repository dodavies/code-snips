#!/usr/bin/env python

# For Darkice streaming // created by Dave/James IP6net 2017.
import time # import time
import os # import OS
import RPi.GPIO as GPIO # import GPIO // Needed <- may need to be installed!!
import logbook # Import logger
logger = logbook.Logger('DJ')
log = logbook.FileHandler('/home/pi/dj.log')
log.push_application()


logger.info("Program started")

state = 0 #bit status


GPIO.setmode(GPIO.BCM) # Set up the GPIO pin type. Board mode.
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Start button
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Stop button


if not os.geteuid() == 0:
    print ("WARNING: You need to run this program as root!!")
    exit()

print ("Welcome, to DJ - Darkice streamer") # Print welcome message.

def startstream():
    global state
    if (state == int(1)):
        time.sleep(2)
        logger.warn("Stream already running!")
        print ("ERROR: Stream already running!")
    else:
        try:
            os.system('darkice &') # run start command
            time.sleep(1)
            print ("Stream started") # Print start message
            logger.info("Stream started")
            state=1
        except:
            print ("ERROR: There has been an issue starting the stream") # error message

def stopstream():
    global state
    if (state == int(0)):
        time.sleep(2)
        logger.warn("Stream already stopped!")
        print ("ERROR: Stream already stopped!")
    else:
        try:
            os.system('killall -9 darkice') # run stop command
            time.sleep(1)
            print ("Stream stopped!") # Print stop message
            logger.info("Stream stopped!")
            state=0
        except:
            print ("ERROR: Can't stop stream") # error message
try:
    while True: # run forever
        if (GPIO.input(23) == 1):
            startstream()
        elif (GPIO.input(24) == 1):
            stopstream()
        else:
            time.sleep(1)

except:
    print ("ERROR: Problem running program!")

finally:
    GPIO.cleanup() # clean up!
    print ("Goodbye!")

