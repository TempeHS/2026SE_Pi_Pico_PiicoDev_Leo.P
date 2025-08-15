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

movement = Navigation(l_servo, r_servo, debug=True)

range_a = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])

while True:
    distance1 = range_a.distance_mm
    distance2 = range_b.distance_mm
    if distance1 <= 100:
        movement.move_r()
    else:
        movement.move_forward()


# while True:
#     distance1 = range_a.distance_mm
#     distance2 = range_b.distance_mm
#     print("Testing navigation")
#     movement.move_forward()
#     if distance1 <= 100 and distance2 > 100:
#         movement.move_r()
#         movement.move_forward()
#     elif distance1 > 100 and distance2 <= 100:
#         movement.move_forward()
#     elif distance1 <= 100 and distance2 <= 100:
#         movement.move_l()
#         movement.move_forward()
#     else:
#         movement.move_forward()