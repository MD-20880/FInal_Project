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


board = [[0,0,0] for i in range(64)]
WIDTH = 8
HEIGHT = 8
curposx = 4
curposy = 4
board[curposy*WIDTH+curposx] = [255,255,255]
sense.set_pixels(board)
    

while True:
    
    for event in sense.stick.get_events():
        sleep(0.3)
        board[curposy*WIDTH+curposx] = [0,0,0]
        if event.direction == 'down':
            curposy += 1
        elif event.direction == 'up':
            curposy -= 1
        elif event.direction == 'left':
            curposx -= 1
        elif event.direction == 'right':
            curposx += 1
        curposx = curposx % 8
        curposy = curposy % 8
        board[curposy*WIDTH+curposx] = [255,255,255]
        sense.clear()
        sense.set_pixels(board)

# led1 = io.LED(17)
# led2 = io.LED(27)

# while True:
#     led1.on()
#     sleep(1)
#     led1.off()
#     led2.on()
#     sleep(1)
#     led2.off()