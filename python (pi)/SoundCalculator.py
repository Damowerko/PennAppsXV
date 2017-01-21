# timestamp, volume of the signal
import Microphone
import coordinate


class SoundCalculator:

    def __init__(self):
        self.microphones = []  # list of microphones
        self.threshold = 300  # the threshold value
        self.sound_collector = []  # list that collects the loudest sound
        # from each mic

    def add_microphone(self, mic):
        # this is a method for adding a microphone to a list of microphones
        self.microphones.append(mic)

    def add_microphone_wrapper(self, usb_port, coord):
        # param: usb_port is the name of the usb port
        # param: coord is the coordinate of the microphone
        # this is a wrapper method for creating new microphones
        self.microphones.append(Microphone(usb_port, coord))

    def collect_sound(self):
        for index, mic in enumerate(self.microphones):
            sound = mic.next()
            if sound >= self.threshold:
                self.sound_collector[index].append(sound - self.threshold)

    def findLoudAngle(self):
        # returns the angle where the loudest sound was heard
        collect_sound()
        max_sound = 0
        angle = -100
        for index, mic in enumerate(self.microphones):
            sound = mic.next()
            if sound >= self.threshold:
                self.sound_collector[index].append(sound - self.threshold)
            if sound >= self.threshold and sound >= max_sound:
                max_sound = sound
                angle = mic.get_angle()
        return angle


def main():
    calc = SoundCalculator()
    mic1 = Microphone('/dev/tty.usbserial', coordinate(5, 0))
    mic2 = Microphone('/dev/tty.usbserial', coordinate(0, 5))
    mic3 = Microphone('/dev/tty.usbserial', coordinate(-5, 0))
    mic4 = Microphone('/dev/tty.usbserial', coordinate(0, -5))
    calc.add_microphone(mic1)
    calc.add_microphone(mic2)
    calc.add_microphone(mic3)
    calc.add_microphone(mic4)
