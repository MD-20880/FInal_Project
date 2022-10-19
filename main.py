#!/user/bin/python

import gpiozero as io
import sense_hat as sense


led1 = io.LED(17)
led2 = io.LED(2)

while True: 
    led1.on()
    io.sleep(1)
    led2.on()
    io.sleep(1)
    led1.off()
    io.sleep(1)
    led2.off()
    io.sleep(1)

