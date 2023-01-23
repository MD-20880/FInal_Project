#!/user/bin/python

debug = True

import sys
if sys.platform == "linux":
    import RPi.GPIO as GPIO
    import gpiozero as io
    from sense_hat import SenseHat
    

from time import sleep
from time import time
import configparser

if not debug:
    import Sensor.Sensor as Sensor
    import Sensor.RpiSensorHat as RpiSensorHat



def init_sensors() -> list:
    #Empty List
    sensorList = []
    
    #Create Sensor Entity to corresponding sensor
    sensehatEntity = RpiSensorHat.RpiSensorHat()
    
    
    #Wrap Sensor Entity in Sensor
    sensehatSensor = Sensor.Sensor(Sensor.SensorType.HumiditySensor, sensehatEntity)
    
    
    
    #Append Sensor to list
    sensorList.append(sensehatSensor)


def loadConfig() ->dict:
    config = configparser.ConfigParser()
    config.read("conf.ini")
    
    

if __name__ == "__main__":
    running = True
    SensorList = init_sensors()
    startSensorsLoop()
    
    while(running):
        dataCollectionLoop()
        frontEndDisplay()
    
    