import RPi.GPIO as GPIO
import time

input_pin = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print(GPIO.input(input_pin))
