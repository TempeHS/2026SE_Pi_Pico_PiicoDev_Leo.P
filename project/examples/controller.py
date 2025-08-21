from navigation import Navigation
from colour import Colour
from screen import Screen
from avoid import Avoid
from PiicoDev_Unified import sleep_ms

class Controller: # goliath
    """
    Class that combines all the subsystems into one file to run
    """
    def __init__(self, debug=False):
        self.__debug = debug
        self.__avoider = Avoid()
        self.__colour = Colour()
        self.__screen = Screen()
        self.__movement = self.__avoider.movement

    def update(self):
        while True:
            if self.__colour.find_green():
                self.__screen.display_stuff("Green :)")
                self.__movement.stop()
                self.__movement.spin()
                self.__movement.move_forward()
                sleep_ms(500)

            distance1 = self.__avoider.range_a.distance_mm
            distance2 = self.__avoider.range_b.distance_mm
            
            if distance1 <= 100 and distance2 > 100:
                self.__screen.display_stuff("Moving Right")
                self.__movement.move_r()
            elif distance1 > 100 and distance2 <= 100:
                self.__screen.display_stuff("Moving Forward")
                self.__movement.move_forward()
            elif distance1 <= 100 and distance2 <= 100:
                self.__screen.display_stuff("Moving Left")
                self.__movement.move_l()
            else:
                self.__screen.display_stuff("Moving Forward")
                self.__movement.move_forward()


IND = Controller()
IND.update()