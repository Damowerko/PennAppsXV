from Microphone import Microphone
from SoundCalculator import SoundCalculator
from coordinate import coordinate
from hardware import arduino
import math
"""
test case suite for SoundCalculator.py
"""


def testRaspberryConnection():
    arduino1 = arduino('/dev/ttyACM1')
    arduino2 = arduino('/dev/ttyACM0')
    arduino1.read()
    arduino2.read()
    print "success"


def main():
    testRaspberryConnection()

main()
