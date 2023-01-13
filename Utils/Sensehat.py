import sys

import RPi.GPIO as GPIO
import gpiozero as io
from sense_hat import SenseHat


from time import sleep
from time import time



sense = SenseHat()


while True:
    # get temperature
    temp =sense.get_temperature()
    # get humidity
    hum =sense.get_humidity()
    # get pressure
    press =sense.get_pressure()
    # get orientation
    orient =sense.get_orientation()
    # get compass
    compass =sense.get_compass()
    # get gyroscope
    gyro =sense.get_gyroscope()
    # get accelerometer
    accel =sense.get_accelerometer()

    print(temp)
    print(hum)
    print(press)
    print(orient)
    print(compass)
    print(gyro)
    print(accel)
    print('\t')

