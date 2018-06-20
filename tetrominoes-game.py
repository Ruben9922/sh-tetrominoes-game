from random import randrange
from time import sleep

from euclid import Point2, Vector2
from sense_emu import SenseHat


class Shape:
    def __init__(self, shape_type, pos, vel):
        self.shape_type = shape_type
        self.pos = pos
        self.vel = vel

    def display(self):
        for point in self.shape_type.points:
            actual_pos = self.pos + point
            sense.set_pixel(actual_pos.x, actual_pos.y, shape_colour)

    def collides(self):
        return False  # Need to implement properly


class ShapeType:
    def __init__(self, points):
        self.points = points

    def compute_width(self):
        max_x = max(point.x for point in self.points)
        min_x = min(point.x for point in self.points)
        return abs(max_x - min_x) + 1

    def compute_height(self):
        max_y = max(point.y for point in self.points)
        min_y = min(point.y for point in self.points)
        return abs(max_y - min_y) + 1


def main():
    global sense, shape_colour
    # Initial setup
    sense = SenseHat()
    # sense.set_rotation(180)
    # sense.low_light = True
    update_interval = 7
    shape_colour = [255, 153, 51]
    background_colour = [0, 0, 0]
    shape_types = [
        ShapeType([
            Point2(0, 0),
            Point2(0, 1),
            Point2(0, 2),
            Point2(0, 3),
        ]),
        ShapeType([
            Point2(0, 0),
            Point2(0, 1),
            Point2(1, 0),
            Point2(1, 1),
        ]),
        ShapeType([
            Point2(0, 0),
            Point2(0, 1),
            Point2(0, 2),
            Point2(1, 1),
        ]),
        ShapeType([
            Point2(0, 0),
            Point2(0, 1),
            Point2(0, 2),
            Point2(1, 0),
        ]),
        ShapeType([
            Point2(0, 0),
            Point2(0, 1),
            Point2(0, 2),
            Point2(1, 2),
        ]),
        ShapeType([
            Point2(0, 1),
            Point2(0, 2),
            Point2(1, 0),
            Point2(1, 1),
        ]),
        ShapeType([
            Point2(0, 0),
            Point2(0, 1),
            Point2(1, 1),
            Point2(1, 2),
        ]),
    ]
    shapes = set()
    count = 0
    while True:
        sense.clear(background_colour)
        # Update shape velocities
        for shape in shapes:
            if shape.collides() or shape.pos.y >= 8 - shape.shape_type.compute_height():
                shape.vel = Vector2(0, 0)

        # Update shape positions based on their updated velocities
        for shape in shapes:
            shape.pos += shape.vel

        # Display shapes
        for shape in shapes:
            shape.display()

        # Set count to zero if update interval exceed
        if count >= update_interval:
            count = 0

        # If interval reached, choose random shape type then add to `moving_shapes` list
        if count == 0:
            shape_type = shape_types[randrange(len(shape_types))]
            pos = Point2(randrange(9 - shape_type.compute_width()), 0)
            initial_vel = Vector2(0, 1)
            shape = Shape(shape_type, pos, initial_vel)
            shapes.add(shape)

        # Increment count and wait
        count += 1
        sleep(0.2)
    # sense.low_light = False


if __name__ == "__main__":
    main()
