from navigation import Navigation
from colour import Colour
from screen import Screen
from avoid import Avoid
from avoid import movement # didnt know u could do this but the internet is a lovely place
from PiicoDev_Unified import sleep_ms
from controller import Controller

# testing controller but wasnt necessary when rest worked
robot = Controller()
robot.update()