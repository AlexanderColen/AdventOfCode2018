import string


def manhattan_Distance(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


def fillGrid(input):
    gridsize = (0, 0)
    coordinates = []
    grid = []
    dot = Coordinate(name='.', x='0', y='0')

    # Determine size of the grid and create all the coordinates.
    for i, coordinate in enumerate(input):
        x = int(coordinate.split(',')[0].strip())
        y = int(coordinate.split(',')[1].strip())

        gridsize = (x, gridsize[1]) if x > gridsize[0] else gridsize
        gridsize = (gridsize[0], y) if y > gridsize[1] else gridsize

        c = Coordinate(name=string.ascii_letters[i], x=x, y=y)
        coordinates.append(c)

    # Place the coordinates in the grid.
    for y in range(gridsize[1]+1):
        row = []
        for x in range(gridsize[0]+1):
            char = '.'
            for c in coordinates:
                if c.x == x and c.y == y:
                    char = c.name
            row.append(char)
        grid.append(row)

    # Place all the surroundings.
    for y_index, row in enumerate(grid):
        new_row = []
        for x_index, x in enumerate(row):
            checking = Coordinate(name='temp', x=x_index, y=y_index)
            closest = checking
            distance = 99999
            for c in coordinates:
                calculated = manhattan_Distance(checking, c)
                # Check if we're checking the coordinate's spot, in that case break out.
                if calculated == 0:
                    closest = c
                    break
                # Check if it's a tie, in that case place the dot.
                if calculated == distance:
                    closest = dot
                # If not, check if it is a new closest.
                elif calculated < distance:
                    closest = c
                    distance = calculated
            new_row.append(closest.name)
        grid[y_index] = new_row

    return grid, coordinates


def puzzle1():
    file_input = open('../Input/input_day6.txt', 'r')
    test_input = ['1, 1', '1, 6', '8, 3', '3, 4', '5, 5', '8, 9']

    # grid, coordinates = fillGrid(test_input)
    grid, coordinates = fillGrid(file_input.readlines())

    d = dict.fromkeys(string.ascii_letters, 0)
    d.update({'.': 0})
    # Print the grid and calculate the area for every Coordinate.
    for i, row in enumerate(grid):
        # print(f'{"{:0>3d}".format(i)}: {row}')
        for c in row:
            d[c] += 1

    # Find all the Coordinates that are on the edge, thus being infinite.
    removeCoordinates = ['.']
    for i, row in enumerate(grid):
        # First and last row are the edge.
        if i == 0 or i == len(grid) - 1:
            for c in row:
                if c not in removeCoordinates:
                    removeCoordinates.append(c)
        # First and last coordinate of this row are on the edge.
        else:
            if row[0] not in removeCoordinates:
                removeCoordinates.append(row[0])
            if row[len(row) - 1] not in removeCoordinates:
                removeCoordinates.append(row[len(row) - 1])

    # Delete all the keys that were on the edge.
    for key in removeCoordinates:
        del d[key]

    return d[max(d, key=lambda key: d[key])]


def puzzle2():
    file_input = open('../Input/input_day6.txt', 'r')
    test_input = ['1, 1', '1, 6', '8, 3', '3, 4', '5, 5', '8, 9']

    # grid, coordinates = fillGrid(test_input)
    grid, coordinates = fillGrid(file_input.readlines())

    region = 0
    for index_y, row in enumerate(grid):
        # print(f'{"{:0>3d}".format(index_y)}: {row}')
        for index_x, x in enumerate(row):
            distance = 0
            point = Coordinate(name='temp', x=index_x, y=index_y)
            for c in coordinates:
                distance += manhattan_Distance(point, c)
            if distance < 10000:
                region += 1

    return region


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
