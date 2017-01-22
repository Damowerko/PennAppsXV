import hardware as hw
import math
from copy import deepcopy


def main():
    horizontal_arduino = hw.arduino("/dev/ttyACM0")
    vertical_arduino = hw.arduino("/dev/ttyACM1")

    while True:
        data = (horizontal_arduino.read(), vertical_arduino.read())

        # check if any of the arduinos did not detect anything
        if data[0] is None or data[1] is None:
            data = None, None
            continue

        angle = calculate_angles(data)
        print angle


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
        angles[0] = math.pi/2.0 + local_angles
    else:
        angles[0] = 3 / 2.0 * math.pi - local_angles[1]

    ignore_vertical = False
    if (angles[0] < math.pi and local_angles[1]<0) or (angles[0] > math.pi and local_angles[1]>0):
        ignore_vertical = True

    if ignore_vertical:
        return angles[0]

    ave = (angles[0] + angles[1])/2.0  # average is used to calculate weights
    w = 0.5
    w_ave = (math.cos(ave)**2)*angles[0]*w + (math.sin(ave)**2)*angles[1]*(1-w)
    return w_ave


def calculate_angle(data, distance):
    c = 340.29
    dt = data[0]

    x = (dt/1000000.0) * c / distance  # x is always positive due to arduino implementation
    if x > 1:
        return math.pi / 2.0
    if x < 1:
        return -math.pi / 2.0
    else:
        return math.asin(x)

if __name__ == '__main__':
    main()