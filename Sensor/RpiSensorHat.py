import Sensor.SensorEntity as SensorEntity
import gpiozero as io
from sense_hat import SenseHat


class RpiSensorHat(SensorEntity):
    
    def __init__(self) -> None:
        self.sense = SenseHat()
        pass
    
    
    
    
    def collect(self) -> dict:
        resultDict = {}
        # get temperature
        temp =self.sense.get_temperature()
        # get humidity
        hum =self.sense.get_humidity()
        # get pressure
        press =self.sense.get_pressure()
        # get orientation
        orient =self.sense.get_orientation()
        # get compass
        compass =self.sense.get_compass()
        # get gyroscope
        gyro =self.sense.get_gyroscope()
        # get accelerometer
        accel =self.sense.get_accelerometer()
        
        resultDict["Temperature"] = temp
        resultDict["Humidity"] = hum
        resultDict["Pressure"] = press
        resultDict["Orientation"] = orient
        resultDict["Compass"] = compass
        resultDict["Gyroscope"] = gyro
        resultDict["Accelerometer"] = accel
        
