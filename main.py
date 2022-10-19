#!/user/bin/python

import gpiozero as io
from sense_hat import SenseHat
from time import sleep
from time import time


sense = SenseHat()


# flash LED panel for n seconds
def flashing(n : int) -> None:
    white = [[255,255,255] for i in range(64)]
    black = [[0,0,0] for i in range(64)]
    start_time = time()
    while time() - start_time < n:
        sense.set_pixels(white)
        sleep(0.1)
        sense.clear()
    sense.clear()


while True:
    # get temperature
    temp = sense.get_temperature()
    # get humidity
    hum = sense.get_humidity()
    # get pressure
    press = sense.get_pressure()
    # get orientation
    orient = sense.get_orientation()
    # get compass
    compass = sense.get_compass()
    # get gyroscope
    gyro = sense.get_gyroscope()
    # get accelerometer
    accel = sense.get_accelerometer()
    

    # print data
    print("Temperature: {}".format(temp))
    print("Humidity: {}".format(hum))
    print("Pressure: {}".format(press))
    print("Orientation: {}".format(orient))
    print("Compass: {}".format(compass))
    print("Gyroscope: {}".format(gyro))
    print("Accelerometer: {}".format(accel))
    print("Magnetometer: {}".format(mag))
    print("Raw: {}".format(raw))

    # flash LED panel for 1 second
    flashing(1)

    # wait 1 second
    sleep(1)
    
        

# led1 = io.LED(17)
# led2 = io.LED(27)

# while True:
#     led1.on()
#     sleep(1)
#     led1.off()
#     led2.on()
#     sleep(1)
#     led2.off()