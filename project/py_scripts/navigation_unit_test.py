from navigation import Navigation
from servo import Servo
from machine import Pin, PWM

r_servo_pwm = PWM(Pin(16))
l_servo_pwm = PWM(Pin(15))

l_servo = Servo(pwm=l_servo_pwm)
r_servo = Servo(pwm=r_servo_pwm)

movement = Navigation(l_servo, r_servo, debug=True)

print("Testing navigation")
movement.move_r()
movement.stop()