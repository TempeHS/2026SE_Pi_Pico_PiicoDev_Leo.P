from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_Unified import sleep_ms

colourSensor = PiicoDev_VEML6040()

class Colour:
    """
    Class for detecting green tiles (victims) and notifying when they have been found 
    """
    def __init__(self, debug=False):
        self.__debug = debug

    def find_green(self):
        data = colourSensor.readHSV()
        hue = data['hue']
        if self.__debug:
            print("Detecting Green")

        if hue >= 75 and hue <= 95: # rough estimate since the sensor is wack + idk what shade of green it needs to find 
            return True
        else:
            return False


# 10 software engineering students VS print("Hello World!")