import RPi.GPIO as GPIO
import time

FRONT_PIN = 18
BACK_PIN = 16
LEFT_PIN = 12
RIGHT_PIN = 10

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RIGHT_PIN, GPIO.OUT)
    GPIO.setup(LEFT_PIN, GPIO.OUT)
    GPIO.setup(FRONT_PIN, GPIO.OUT)
    GPIO.setup(BACK_PIN, GPIO.OUT)

def pulseMotor(PIN):
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(.4)
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(PIN, GPIO.LOW)


def pulseFrontMotor():
    pulseMotor(FRONT_PIN)

def pulseBackMotor():
    pulseMotor(BACK_PIN)

def pulseLeftMotor():
    pulseMotor(LEFT_PIN)

def pulseRightMotor():
    pulseMotor(RIGHT_PIN)
