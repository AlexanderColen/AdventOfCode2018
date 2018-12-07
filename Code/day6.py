import string
import numpy as np

def puzzle1():
    file_input = open('../Input/input_day6.txt', 'r')

    test_input = ['1, 1', '1, 6', '8, 3', '3, 4', '5, 5', '8, 9']
    gridsize = (0, 0)
    coordinates = []

    # Determine size of the grid.
    for i, coordinate in enumerate(test_input):
        x = int(coordinate.split(',')[0].strip())
        y = int(coordinate.split(',')[1].strip())

        gridsize = (x, gridsize[1]) if x > gridsize[0] else gridsize
        gridsize = (gridsize[0], y) if y > gridsize[1] else gridsize

        coordinates.append(Coordinate(name=string.ascii_letters[i], x=x, y=y))

    for c in coordinates:
        print(c)

    return 0


def puzzle2():
    file_input = open('../Input/input_day6.txt', 'r')

    return 0


class Coordinate:
    def __init__(self, name, x, y):
        # Create all variables set them to the parameters.
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f'Name: {self.name} - X: {self.x} - Y: {self.y}'


print(f'Puzzle 1 outcome: {puzzle1()}')
print(f'Puzzle 2 outcome: {puzzle2()}')
