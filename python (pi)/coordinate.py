
import math


class coordinate:
    """
    The coordinate class is used to place the microphones in a coordinate system. The class can calculate the angle difference between any two coordinates.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = math.sqrt(x * x + y * y)
        if x == 0 :
            if y > 0 : 
                self.angle = 3.14159265358797323 / 2
            elif y < 0 :
                self.angle = -3.14159265358797323 / 2
            else :
                self.angle = 0
        else :
            self.angle = math.atan(y / float(x))
        # angle is in radians

    def findAngle(self, coord):
        # param: coord is another coordinate.
        # return: The angle between the microphones.
        return math.abs(self.angle - coord.get_angle)

    def get_angle(self):
        # return: The angle of the coordinate
        return self.angle

    def get_magnitude(self):
        # return: The magnitude of the coordinate
        return self.magnitude
