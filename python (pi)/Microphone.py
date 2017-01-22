import serial
import coordinate


class Microphone:
    """
    Contains a buffer that has all the 64 byte info. The buffer will read off
    all the data that the arduino recorded.
    """

    def __init__(self, usb_port, coord):
        self.usb_port = usb_port
        self.coord = coord
        self.angle = coord.get_angle()
        self.serial = ''#serial.Serial(usb_port, 9600)
        self.buffer = []
        self.dt = 0  # the difference in time between updates

    def set_buffer(self, test_list):
    # this method is for testing use only
        self.buffer = test_list

    def read(self):
        """
        Do 64 byte processing here
        Update self.dt
        return true if the buffer updated and false otherwise
        """
        return false

    def write(self, intensity, duration, buzzer_id):
        """
        Writes to the buzzer with the given intensity and duration
        Message format: intensity, duration, buzzer_id
        """
        message = str(intensity) + ',' + str(duration) + ',' + str(buzzer_id)
        self.serial.write(message)

    def hasNext(self):
        # return: true if there is another sound in the buffer and false
        # otherwise
        return len(self.buffer) != 0

    def next(self):
        # return: The next sound level in the buffer
        if not self.hasNext():
            return -1
        temp = self.buffer[0]
        del self.buffer[0]
        return temp

    def get_angle(self):
        return self.angle

    def get_coord(self):
        return self.get_coord

def createMic(usb_port, coord):
    return Microphone(usb_port, coord)
