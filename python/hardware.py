import serial


class arduino:
    """
    This is the class for reading arduino serial output
    """

    def __init__(self, usb_port):
        self.serial = serial.Serial(
            usb_port, 115200, bytesize=serial.EIGHTBITS)
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
        byte1 = self.serial.read()
        byte2 = self.serial.read()
        byte3 = self.serial.read()
        dt = int(byte1, 2)
        return false