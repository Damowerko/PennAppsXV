from Microphone import Microphone
from SoundCalculator import SoundCalculator
from coordinate import coordinate
from hardware import arduino
import math
"""
test case suite for SoundCalculator.py
"""


def testRaspberryConnection():
    arduino1 = arduino('dev/ttyAMC0')
    print "success"


def main():
    testRaspberryConnection()

main()
