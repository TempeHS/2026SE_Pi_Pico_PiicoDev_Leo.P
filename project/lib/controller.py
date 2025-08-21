from navigation import Navigation
from colour import Colour
from screen import Screen
from avoid import Avoid
from avoid import movement # didnt know u could do this but the internet is a lovely place
from PiicoDev_Unified import sleep_ms

class Controller: # goliath
    def __init__(self, debug=False):
        self.__debug = debug
        self.__avoider = Avoid()
        self.__colour = Colour()
        self.__screen = Screen()
        self.__movement = movement

    def update(self):
        while True:
            green = self.__colour.find_green()
            if green:
                self.__screen.display_stuff("Green :)")
                self.__movement.stop()
                self.__movement.spin()
                self.__movement.move_forward()

            distance1 = self.__avoider.range_a.dista    nce_mm
            distance2 = self.__avoider.range_b.distance_mm
            
            if distance1 <= 100 and distance2 > 100:
                self.__movement.move_r()
                self.__screen.display_stuff("Moving Right")
            elif distance1 > 100 and distance2 <= 100:
                self.__movement.move_forward()
                self.__screen.display_stuff("Moving Forward")
            elif distance1 <= 100 and distance2 <= 100:
                self.__movement.move_l()
                self.__screen.display_stuff("Moving Left")
            else:
                self.__movement.move_forward()
                self.__screen.display_stuff("Moving Forward")

if __name__ == "__main__":
    robot = Controller()
    robot.update()