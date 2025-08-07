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

def turn_l():
    while True:
        # r wheel
        my_servo.set_duty(2500)
        # l wheel
        l_my_servo.set_duty(2500)
        time.sleep(2)