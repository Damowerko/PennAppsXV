import hardware as hw
import math
from copy import deepcopy
from Visualize import *


def main():
    horizontal_arduino = hw.arduino("/dev/ttyACM0")
    vertical_arduino = hw.arduino("/dev/ttyACM2")

    visualize = Visualize()

    while True:
        data = (horizontal_arduino.read(), vertical_arduino.read())
        print data

        # check if any of the arduinos did not detect anything
        if data[0] is None or data[1] is None:
            data = None, None
            continue

        angle = calculate_angles(data)
        visualize.draw(angle)
        print angle * 180/math.pi


def calculate_angles(data):
    h_distance = 0.3556  # TODO: measure distance
    v_distance = 0.2286

    local_angles = [calculate_angle(data[0], h_distance), calculate_angle(data[1], v_distance)]

    angles = deepcopy(local_angles)

    if local_angles[0] > 0:
        angles[1] = math.pi - local_angles[1]
    elif local_angles[1] < 0:
        angles[1] = 2*math.pi + local_angles[1]

    if local_angles[1] > 0:
        angles[0] = math.pi/2.0 + local_angles[0]
    else:
        angles[0] = 3 / 2.0 * math.pi - local_angles[0]

    print "Local angles: ",local_angles[0], local_angles[1]
    print "Angles: ", angles[0], angles[1]

    ignore_vertical = False
    if (angles[0] < math.pi and local_angles[1]<0) or (angles[0] > math.pi and local_angles[1]>0):
        ignore_vertical = False

    if ignore_vertical:
        return angles[0]

    ave = (angles[0] + angles[1])/2.0  # average is used to calculate weights
    print "average: ", ave
    w_ave = (math.cos(ave)**2)*angles[0] + (math.sin(ave)**2)*angles[1]
    return w_ave


def calculate_angle(data, distance):
    c = 340.29
    dt = data

    x = (dt/1000000.0) * c / distance  # x is always positive due to arduino implementation
    if x > 1:
        return math.pi / 2.0
    if x < -1:
        return -math.pi / 2.0
    else:
        return math.asin(x)

if __name__ == '__main__':
    main()