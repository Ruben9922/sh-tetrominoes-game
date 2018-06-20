from random import randrange
from time import sleep

from euclid import Point2, Vector2
from sense_emu import SenseHat


class Shape:
    shape_colour = [255, 153, 51]

    def __init__(self, shape_type, pos, vel):
        self.shape_type = shape_type
        self.pos = pos
        self.vel = vel

    def display(self):
        for point in self.shape_type.points:
            actual_pos = self.pos + point
            if 0 <= actual_pos.x <= 7 and 0 <= actual_pos.y <= 7:
                sense.set_pixel(actual_pos.x, actual_pos.y, self.shape_colour)

    def collides(self, shapes):
        max_x = max(point.x for point in self.shape_type.points)
        for x in range(max_x):  # For each column
            column = (point for point in self.shape_type.points if point.x == x)
            lowest_point = max(column, key=lambda point: point.y)  # Point with the highest y-value in the column
            lowest_point_wc = lowest_point + self.pos

            for shape in shapes:
                if shape != self:  # Don't compare to itself
                    for point in shape.shape_type.points:
                        point_wc = point + shape.pos
                        if point_wc - lowest_point_wc == Vector2(0, 1):
                            return True
        return False


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
    global sense

    # Initial setup
    sense = SenseHat()
    # sense.set_rotation(180)
    # sense.low_light = True

    update_interval = 7
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
            if shape.pos.y >= 8 - shape.shape_type.compute_height() or shape.collides(shapes):
                shape.vel = Vector2(0, 0)

        # Update shape positions based on their updated velocities
        for shape in shapes:
            shape.pos += shape.vel

        # Set count to zero if update interval exceed
        if count >= update_interval:
            count = 0

        # If interval reached, choose random shape type then add to `moving_shapes` list
        if count == 0:
            shape_type = shape_types[randrange(len(shape_types))]
            pos = Point2(randrange(9 - shape_type.compute_width()), 1 - shape_type.compute_height())
            initial_vel = Vector2(0, 1)
            shape = Shape(shape_type, pos, initial_vel)
            shapes.add(shape)

        # Display shapes
        for shape in shapes:
            shape.display()

        # Increment count and wait
        count += 1
        sleep(1)
    # sense.low_light = False


if __name__ == "__main__":
    main()
