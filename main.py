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
    for event in sense.stick.get_events():
        print(event.direction, event.action)  


# led1 = io.LED(17)
# led2 = io.LED(27)

# while True:
#     led1.on()
#     sleep(1)
#     led1.off()
#     led2.on()
#     sleep(1)
#     led2.off()