from Microphone import Microphone
from SoundCalculator import SoundCalculator
from coordinate import coordinate
import math
"""
test case suite for SoundCalculator.py
"""


def getMicrophones():
    mic1 = Microphone('/dev/tty.usbserial', coordinate(5, 0))
    mic2 = Microphone('/dev/tty.usbserial', coordinate(0, 5))
    mic3 = Microphone('/dev/tty.usbserial', coordinate(-5, 0))
    mic4 = Microphone('/dev/tty.usbserial', coordinate(0, -5))
    return [mic1, mic2, mic3, mic4]


def test0buffer():
    microphones = getMicrophones()
    calc = SoundCalculator()
    microphones[0].set_buffer([0, 0, 0, 0])
    microphones[1].set_buffer([0, 0, 0, 0])
    microphones[2].set_buffer([0, 0, 0, 0])
    microphones[3].set_buffer([0, 0, 0, 0])
    for mic in microphones:
        calc.add_microphone(mic)
    angle = calc.findLoudestAngle()
    assert(angle == -100)
    print "test0buffer passed"


def testUnderThreshold():
    microphones = getMicrophones()
    calc = SoundCalculator()
    microphones[0].set_buffer([100, 100, 100, 200])
    microphones[1].set_buffer([200, 250, 100, 100])
    microphones[2].set_buffer([100, 100, 0, 0])
    microphones[3].set_buffer([0, 0, 0, 0])
    for mic in microphones:
        calc.add_microphone(mic)
    angle = calc.findLoudestAngle()
    assert(angle == -100)
    print "testUnderThreshold passed"


def testOneMicAboveThreshold():
    microphones = getMicrophones()
    calc = SoundCalculator()
    microphones[0].set_buffer([400, 400, 100, 200])
    microphones[1].set_buffer([200, 250, 100, 100])
    microphones[2].set_buffer([100, 100, 0, 0])
    microphones[3].set_buffer([0, 0, 0, 0])
    for mic in microphones:
        calc.add_microphone(mic)
    angle = calc.findLoudestAngle()
    assert(angle == math.radians(0))
    print "testOneMicAboveThreshold passed"


def testOneMicAboveThreshold2():
    microphones = getMicrophones()
    calc = SoundCalculator()
    microphones[0].set_buffer([100, 100, 100, 200])
    microphones[1].set_buffer([600, 250, 600, 100])
    microphones[2].set_buffer([100, 100, 0, 0])
    microphones[3].set_buffer([0, 0, 0, 0])
    for mic in microphones:
        calc.add_microphone(mic)
    angle = calc.findLoudestAngle()
    assert(math.fabs(angle - math.radians(90)) < 0.00001)
    print "testOneMicAboveThreshold2 passed"


def testTwoMicsAboveThreshold():
    microphones = getMicrophones()
    calc = SoundCalculator()
    microphones[0].set_buffer([600, 100, 100, 200])
    microphones[1].set_buffer([600, 250, 600, 100])
    microphones[2].set_buffer([100, 100, 0, 0])
    microphones[3].set_buffer([0, 0, 0, 0])
    for mic in microphones:
        calc.add_microphone(mic)
    angle = calc.findLoudestAngle()
    assert(math.fabs(angle - math.radians(45)) < 0.00001)
    print "testTwoMicsAboveThreshold passed"


def testTwoMicsAboveThreshold2():
    microphones = getMicrophones()
    calc = SoundCalculator()
    microphones[0].set_buffer([600, 100, 100, 200])
    microphones[1].set_buffer([100, 250, 100, 100])
    microphones[2].set_buffer([100, 100, 0, 0])
    microphones[3].set_buffer([600, 0, 0, 0])
    for mic in microphones:
        calc.add_microphone(mic)
    angle = calc.findLoudestAngle()
    assert(math.fabs(angle - math.radians(-45)) < 0.00001)
    print "testTwoMicsAboveThreshold2 passed"


def main():
    test0buffer()
    testUnderThreshold()
    testOneMicAboveThreshold()
    testOneMicAboveThreshold2()
    testTwoMicsAboveThreshold()
    testTwoMicsAboveThreshold2()

main()
