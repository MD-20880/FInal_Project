#!/user/bin/python

import gpiozero as io
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
while True: 
    X = [255,255,255]
    O = [0,0,0]
    question_mark = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]
    sense.set_pixels(question_mark)

