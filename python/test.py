from Microphone import Microphone
from SoundCalculator import SoundCalculator
from coordinate import coordinate
from hardware import arduino
import math
"""
test case suite for SoundCalculator.py
"""


def testRaspberryConnection():
    #arduino1 = arduino('/dev/ttyAMA0')
    arduino2 = arduino('/dev/ttyACM0')
    arduino2.read()
    print "success"


def main():
    testRaspberryConnection()

main()
