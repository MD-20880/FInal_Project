#!/user/bin/python

import gpiozero as io
import sense_hat as sense
from time import sleep

led1 = io.LED(17)
led2 = io.LED(27)

while True: 
    led1.on()
    sleep(0.5)
    led2.on()
    sleep(0.5)
    led1.off()
    sleep(0.5)
    led2.off()
    sleep(0.5)
    print("Done cycle")

