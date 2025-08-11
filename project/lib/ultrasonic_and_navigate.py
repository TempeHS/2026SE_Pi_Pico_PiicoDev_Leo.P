from machine import Pin, PWM
from servo import Servo
import time
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms
from navigation import Navigation

r_servo_pwm = PWM(Pin(16))
l_servo_pwm = PWM(Pin(15))

l_servo = Servo(pwm=l_servo_pwm)
r_servo = Servo(pwm=r_servo_pwm)

range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])

movement = Navigation(l_servo, r_servo, debug=True)

class Ultrasonic:
    def __init__(self, l_servo, r_servo, debug=False):
        self.__l_servo = l_servo
        self.__r_servo = r_servo
        self.__debug = debug

while True:
    distance1 = range_a.distance_mm
    distance2 = range_b.distance_mm
    if distance1 <= 20 or distance2 <=20:
            movement.stop()