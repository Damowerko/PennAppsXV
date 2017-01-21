# timestamp, volume of the signal
import Microphone
import coordinate


class SoundCalculator2:

    def __init__(self):
        self.microphones = []  # list of microphones
        self.threshold = 300  # the threshold value
        # self.sound_collector = []  # list that collects the loudest sound
        # from each mic

    def add_microphone(self, mic):
        # this is a method for adding a microphone to a list of microphones
        self.microphones.append(mic)

    def add_microphone_wrapper(self, usb_port, coord):
        # param: usb_port is the name of the usb port
        # param: coord is the coordinate of the microphone
        # this is a wrapper method for creating new microphones
        self.microphones.append(Microphone(usb_port, coord))

    def findLoudestAngle(self):
        