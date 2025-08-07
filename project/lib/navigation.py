from machine import Pin, PWM
from servo import Servo
import time

servo_pwm = PWM(Pin(16))
l_servo_pwm = PWM(Pin(15))

freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

my_servo = Servo(pwm=servo_pwm)
l_my_servo = Servo(pwm=l_servo_pwm)

class Navigation:
    def __init__(self, forward, backward, left, right, spin, stop, debug=False):
        self.__forward = forward
        self.__backward = backward
        self.__left = left
        self.__right = right
        self.__spin = spin
        self.__stop = stop
        self.__debug = debug

    def move_forward(self):
        if self.__debug:
            print("Going Forward")
        l_my_servo.set_duty(2500)
        my_servo.set_duty(500)
        time.sleep(2)

    def move_backward(self):
        if self.__debug:
            print("Going Backward")
        l_my_servo.set_duty(500)
        my_servo.set_duty(2500)
        time.sleep(2)

    def move_l(self):
        if self.__debug:
            print("Turning Left")
        l_my_servo.set_duty(1500)
        my_servo.set_duty(2500)
        time.sleep(2)

    def move_r(self):
        if self.__debug:
            print("Turning Right")
        l_my_servo.set_duty(500)
        my_servo.set_duty(1500)
        time.sleep(2)

    def spin(self):
        if self.__debug:
            print("Spinning")
        l_my_servo.set_duty(2500)
        my_servo.set_duty(2500)

    def stop(self):
        if self.__debug:
            print("Stopped")
        l_my_servo.set_duty(1500)
        my_servo.set_duty(1500)