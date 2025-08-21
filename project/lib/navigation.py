from machine import Pin, PWM
from servo import Servo
import time
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms

# instantiation
r_servo_pwm = PWM(Pin(16))
l_servo_pwm = PWM(Pin(15))

freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

l_servo = Servo(pwm=l_servo_pwm)
r_servo = Servo(pwm=r_servo_pwm)

#
class Navigation:
    """
    Class that sets different ways for the IND to navigate
    """
    def __init__(self, l_servo, r_servo, debug=False):
        self.__l_servo = l_servo
        self.__r_servo = r_servo
        self.__debug = debug

    def move_forward(self):
        if self.__debug:
            print("Going Forward")
        self.__l_servo.set_duty(2500)
        self.__r_servo.set_duty(500)

    def move_backward(self):
        if self.__debug:
            print("Going Backward")
        self.__l_servo.set_duty(500)
        self.__r_servo.set_duty(2500)

    def move_r(self):
        if self.__debug:
            print("Turning Right")
        self.__l_servo.set_duty(1500)
        self.__r_servo.set_duty(1760)
        time.sleep(2)

    def move_l(self):
        if self.__debug:
            print("Turning Left")
        self.__l_servo.set_duty(1260)
        self.__r_servo.set_duty(1500)
        time.sleep(2)

    def spin(self):
        if self.__debug:
            print("Spinning")
        self.__l_servo.set_duty(2500)
        self.__r_servo.set_duty(2500)
        time.sleep(2)

    def stop(self):
        if self.__debug:
            print("Stopped")
        self.__l_servo.set_duty(1500)
        self.__r_servo.set_duty(1500)