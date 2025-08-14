from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_Unified import sleep_ms

colourSensor = PiicoDev_VEML6040()

class Colour:
    def __init__(self, colour, debug=False):
        self.__colour = colour
        self.__debug = debug

    def find_green(self):
        if self.__debug:
            print("Detecting Green")
        self.__colour
        while True:
            data = colourSensor.readHSV()
            hue = data['hue']
            print(str(label) + " Hue: " + str(hue))

# 10 software engineering students VS print("Hello World!")