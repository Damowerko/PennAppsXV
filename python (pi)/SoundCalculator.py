# timestamp, volume of the signal
import Microphone
import coordinate


class SoundCalculator:

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

    def collect_sound(self):
        sound_collector = []
        for index, mic in enumerate(self.microphones):
            sound_collector.append([])
            while mic.hasNext():
                sound = mic.next()
                if sound >= self.threshold:
                    sound_collector[index].append(sound - self.threshold)
        return sound_collector

    def find_highest_index(self, l):
        # finds the index of the highest element of the list
        index = -1
        highest = 0
        for i, elem in enumerate(l):
            if elem > highest:
                highest = elem
                index = i
        return index

    def average(self, l):
        if len(l) == 0:
            return 0
        return sum(l) / float(len(l))

    def findLoudestAngle(self):
        # returns the angle where the loudest sound was heard
        sound_collector = self.collect_sound()
        average_sound = []
        for collection in sound_collector:
            average_sound.append(self.average(collection))

        loudest_mic_index = self.find_highest_index(average_sound)

        #if there is no loudest sound, there sound't be a buzzer
        if loudest_mic_index == -1 :
            return -100

        loudest_sound = average_sound[loudest_mic_index]
        del average_sound[loudest_mic_index]
        second_loudest_mic_index = self.find_highest_index(average_sound)
        
        #if there is no second loudest sound, then buzz the first index
        if second_loudest_mic_index == -1:
            return self.microphones[loudest_mic_index].get_angle()

        second_loudest_sound = average_sound[second_loudest_mic_index]
        if second_loudest_mic_index >= loudest_mic_index:
            second_loudest_mic_index += 1

        # if the seocnd_loudest sound is insignificant then ignore the second
        # loudest sound
        if(loudest_sound - second_loudest_sound > 50):
            return self.microphones[loudest_mic_index].get_angle()

        # otherwise average the angles
        angle = self.microphones[loudest_mic_index].get_angle(
        ) + self.microphones[second_loudest_mic_index].get_angle()
        return angle / 2.0


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
