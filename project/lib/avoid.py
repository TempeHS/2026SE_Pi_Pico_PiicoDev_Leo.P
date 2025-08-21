from machine import Pin, PWM
from servo import Servo
import time
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms
from navigation import Navigation

class Avoid:
    """
    Class to avoid colliding with walls / obstacles
    """
    def __init__(self, debug=False):
        self.__debug = debug

        r_servo_pwm = PWM(Pin(16))
        l_servo_pwm = PWM(Pin(15))

        l_servo = Servo(pwm=l_servo_pwm)
        r_servo = Servo(pwm=r_servo_pwm)

        self.range_a = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])
        self.range_b = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])

        self.movement = Navigation(l_servo, r_servo, debug=True)

    def avoid(self):
        if self.__debug:
            print("Testing obstacle detection")
        while True:
            distance1 = self.range_a.distance_mm
            distance2 = self.range_b.distance_mm
            if distance1 <= 100 and distance2 > 100:
                self.movement.move_r()
            elif distance1 > 100 and distance2 <= 100:
                self.movement.move_forward()
            elif distance1 <= 100 and distance2 <= 100:
                self.movement.move_l()
            else:
                self.movement.move_forward()