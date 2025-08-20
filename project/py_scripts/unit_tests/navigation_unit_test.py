### navigation unit test
from machine import Pin, PWM
from servo import Servo
from time import sleep
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms
from navigation import Navigation
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_SSD1306 import *

#
r_servo_pwm = PWM(Pin(16))
l_servo_pwm = PWM(Pin(15))

l_servo = Servo(pwm=l_servo_pwm)
r_servo = Servo(pwm=r_servo_pwm)

movement = Navigation(l_servo, r_servo, debug=True)

# test
movement.move_forward()
movement.move_backward()
movement.move_l()
movement.move_r()
movement.stop()
movement.move_spin()