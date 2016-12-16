from sense_hat import SenseHat
from time import sleep

def display_shape(shape, originX, originY, clear = False):
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if (shape[i][j]):
                x = originX + j
                y = originY + i
                sense.set_pixel(x, y, background_colour if clear else shape_colour)

def clear_shape(shape, originX, originY):
    display_shape(shape, originX, originY, True)

sense = SenseHat()
sense.set_rotation(180)
sense.clear() # Temporarily moved this for quicker testing
sense.low_light = True

shape_colour = [255, 153, 51]
background_colour = [0, 0, 0]
shapes = [
    [
        [True, True, True, True]
    ],
    [
        [True, True],
        [True, True]
    ],
    [
        [True, True, True],
        [False, True]
    ],
    [
        [True, True, True],
        [True]
    ],
    [
        [True, True, True],
        [False, False, True]
    ],
    [
        [False, True, True],
        [True, True]
    ],
    [
        [True, True],
        [False, True, True]
    ]
]

for i in range(len(shapes)):
    display_shape(shapes[i], 0, 0)
    sleep(0.5)
    clear_shape(shapes[i], 0, 0)
    sleep(0.1)

sense.low_light = False
