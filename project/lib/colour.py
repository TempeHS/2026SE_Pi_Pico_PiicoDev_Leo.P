from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_Unified import sleep_ms

colourSensor = PiicoDev_VEML6040()

class colour:
    def __init__(self, red, grn, blu, debug=False):
        self.__red = red
        self.__grn = grn
        self.__blu = blu
        self.__debug = debug
    
while True:
    data = colourSensor.readRGB()
    red = data['red']
    grn = data['green']
    blu = data['blue']
    
    print(str(blu) + " Blue  " + str(grn) + " Green  " + str(red) + " Red")
    sleep_ms(1000)