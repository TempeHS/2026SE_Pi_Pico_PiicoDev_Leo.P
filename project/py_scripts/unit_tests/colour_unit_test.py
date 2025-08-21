### colour sensor unit test
from machine import Pin, PWM
from servo import Servo
from time import sleep
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms
from navigation import Navigation
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_SSD1306 import *

# test
colourSensor = PiicoDev_VEML6040()
print("Testing colour sensor")
while True:
    data = colourSensor.readHSV()
    hue = data['hue']
    if hue >= 75 and hue <= 95:
        print("Found Green", hue)
    else:
        print("No Green Found", hue)

    # figure out what it sees as green

    sleep_ms(300)