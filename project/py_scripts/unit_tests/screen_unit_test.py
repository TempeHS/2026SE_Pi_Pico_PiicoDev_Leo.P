### lcd screen unit test
from machine import Pin, PWM
from servo import Servo
from time import sleep
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms
from navigation import Navigation
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_SSD1306 import *

# unit test
display = create_PiicoDev_SSD1306()
display.fill(0)
display.text("PiicoDev", 0, 20, 1)
display.text("test words", 0, 40, 1)
display.show()

# incase forget: 
    # 1st number = x, 2nd = y, 3rd = black/white