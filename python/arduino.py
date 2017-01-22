import serial


class arduino:
	"""
	This is the class for reading arduino serial output
	"""
    def __init__(self, usb_port):
        self.serial = serial.Serial(usb_port, 9600)
        self.dir = 'N'
        self.dt = 0  # the difference in time between updates
        self.microphones = [] # the microphones attached to this arduino

    def read(self):
        """
        only 4 bytes in readlines
        first 2 bytes is an int = dt
        next byte is a char = dir
        last bye is end of steam = '\n'
        """
        b = serial.readlines()
        return false
