from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(180)
sense.low_light = True

shape_colour = [255, 153, 51]
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

sense.clear()
sense.low_light = False
