import hardware as hw
import math
from copy import deepcopy
from Visualize import *
from time import time

global horizontal_arduino
global vertical_arduino

def main():
    global horizontal_arduino
    global vertical_arduino

    horizontal_arduino = hw.arduino("/dev/ttyACM0")
    vertical_arduino = hw.arduino("/dev/ttyACM2")

    visualize = Visualize()

    lastvibrate = time()

    while True:
        data = (horizontal_arduino.read(), vertical_arduino.read())
        print data

        # check if any of the arduinos did not detect anything
        if data[0] is None or data[1] is None:
            data = None, None
            continue

        angle = calculate_angles(data)
        visualize.draw(angle)

        if time() - lastvibrate > 3:
            vibrate(angle)
            lastvibrate = time()
        print angle * 180/math.pi


def calculate_angles(data):
    h_distance = 0.3429  # TODO: measure distance
    v_distance = 0.2413

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


def vibrate(angle):
    global horizontal_arduino
    global vertical_arduino


    import hardware as hw

    horizontal_arduino = hw.arduino("/dev/ttyACM0")
    vertical_arduino = hw.arduino("/dev/ttyACM2")

    def write(n):
        if n==0 or n==4:
            vertical_arduino.write('A')
        elif n==1:
            vertical_arduino.write('B')
        elif n==2:
            horizontal_arduino.write('A')
        elif n==3:
            horizontal_arduino.write('B')

    angle = angle + math.pi*3.0/5.0
    angle = angle + math.pi
    if angle > math.pi*2:
        angle = angle - math.pi*2
    eigth = int(4*angle/math.pi+0.49)

    if (eigth % 2 == 1):
        write((eigth+1)/2)
        write((eigth-1)/2)
    else:
        write(eigth/2)



if __name__ == '__main__':
    main()