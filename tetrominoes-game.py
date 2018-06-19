from random import randrange
from time import sleep

from sense_emu import SenseHat


def display_shape(shape, originX, originY, clear = False):
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j]:
                x = originX + j
                y = originY + i
                sense.set_pixel(x, y, background_colour if clear else shape_colour)


def clear_shape(shape, originX, originY):
    display_shape(shape, originX, originY, True)


def translate_shape(shape, sourceOriginX, sourceOriginY, destOriginX, destOriginY):
    clear_shape(shape, sourceOriginX, sourceOriginY)
    display_shape(shape, destOriginX, destOriginY)


def compute_width(shape):
    max_width = 0
    for i in range(len(shape)):
        current_width = len(shape[i])
        if (current_width > max_width):
            max_width = current_width
    return max_width


def is_shape_underneath(shape, originX, originY):
    return False  # Need to implement properly


# Initial setup
sense = SenseHat()
sense.set_rotation(180)
# sense.low_light = True

ADD_SHAPE_INTERVAL = 7

shape_colour = [255, 153, 51]
background_colour = [0, 0, 0]
shape_types = [
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
moving_shapes = []
still_shapes = []
count = 0

sense.clear(background_colour)
while True:
    # Move shapes in `moving_shapes` down by 1
    for shape in moving_shapes:
        if ((not is_shape_underneath(shape[0], shape[1], shape[2]))
                and (shape[2] < 8 - len(shape[0]))):
            clear_shape(shape[0], shape[1], shape[2])
            shape[2] += 1
            display_shape(shape[0], shape[1], shape[2])
        else:
            moving_shapes.remove(shape)
            still_shapes.append(shape)

    # Set count to zero if reached `ADD_SHAPE_INTERVAL`
    if count >= ADD_SHAPE_INTERVAL:
        count = 0

    # If interval reached, choose random shape type then add to `moving_shapes` list
    if count == 0:
        shape = shape_types[randrange(len(shape_types))]
        originX = randrange(9 - compute_width(shape))
        originY = 0
        display_shape(shape, originX, originY)
        moving_shapes.append([shape, originX, originY])

    # Increment count and wait
    count += 1
    sleep(0.2)

# sense.low_light = False
