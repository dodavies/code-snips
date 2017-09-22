# For Darkice streaming // created by Dave/James IP6net 2017.
import time # import time
import os # import OS
import RPi.GPIO as GPIO # import GPIO // Needed <- may need to be installed!!


GPIO.setmode(GPIO.BCM) # Set up the GPIO pin type. Board mode.
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Start button
GPIO.setup(24, GPIO.IN, pulll_up_down = GPIO.PUD_DOWN) # Stop button

print ("Welcome, to DJ - Darkice streamer") # Print welcome message.

def startsteam():
    try:
        os.system('') # run start command
        print ("Stream started") # Print start message
    except:
        print ("ERROR: There has been an issue starting the stream") # error message

def stopstream():
    try:
        os.system('') # run stop command
        print ("Stream stopped!") # Print stop message
    except:
        print ("ERROR: Can't stop stream") # error message


while True: # run forever
    if (GPIO.input(23) == 1):
        startstream()
    elif (GPIO.input(24) == 1):
        stopstream()
    else:
        time.sleep(1)
