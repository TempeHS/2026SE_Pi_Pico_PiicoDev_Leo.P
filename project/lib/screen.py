from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms

display = create_PiicoDev_SSD1306()

class Screen:
    """
    Class to display the state of the robot on the lcd screen
    """
    def __init__(self, debug=False):
        self.__debug = debug

    def display_stuff(self, thing):
        if self.__debug:
            print("Testing screen")
        display.fill(0)
        display.text("Currently:", 0, 20, 1)
        display.text(thing, 0, 40, 1)
        display.show()
    
    sleep_ms(500)