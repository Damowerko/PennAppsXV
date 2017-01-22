import serial


class arduino:
    """
    This is the class for reading arduino serial output
    """

    def __init__(self, usb_port):
        self.serial = serial.Serial(
            usb_port, 115200, bytesize=serial.EIGHTBITS, timeout=3)
        self.dir = None
        self.dt = None  # the difference in time between updates
        self.microphones = []  # the microphones attached to this arduino

    def read(self):
        """
        only 4 bytes in readlines
        first 2 bytes is an int = dt
        next byte is a char = dir
        last bye is end of steam = '\n'
        """
        line = self.serial.readline()
        if line != '':
            out = int(line.split('\r')[0])
            return out
        return None

    def write(self, data):
        input = data
        self.serial.write(input)
        print "write: ", input
        return None
