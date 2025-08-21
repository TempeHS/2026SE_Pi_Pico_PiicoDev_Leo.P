### collision avoidance unit test
from machine import Pin, PWM
from servo import Servo
from time import sleep
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms
from navigation import Navigation
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_SSD1306 import *

r_servo_pwm = PWM(Pin(16))
l_servo_pwm = PWM(Pin(15))

l_servo = Servo(pwm=l_servo_pwm)
r_servo = Servo(pwm=r_servo_pwm)

range_a = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])

movement = Navigation(l_servo, r_servo, debug=True)

# unit test
while True:
    distance1 = range_a.distance_mm
    distance2 = range_b.distance_mm
    if distance1 <= 100 and distance2 > 100:
        movement.move_r()
        print("moved right")
    elif distance1 > 100 and distance2 <= 100:
        movement.move_forward()
        print("moved forward")
    elif distance1 <= 100 and distance2 <= 100:
        movement.move_l()
        print("moved left")
    else:
        movement.move_forward()
        print("moved forward")
    #sleep(.5)

# removed the sleep because there was other issues with the previous code which made it require a sleep but with the issues fixed having a sleep at the end only makes it more prone to crashing into obstacles