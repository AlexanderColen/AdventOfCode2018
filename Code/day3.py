def fillGrid(width=1000, height=1000):
    file_input = open('../Input/input_day3.txt', 'r')

    # Define grid.
    grid = {}
    for x in range(width):
        for y in range(height):
            grid[(x, y)] = 0

    for line in file_input:
        line = line.strip('\n')

        # Fetch the specific instructions from the line.
        ID = int(line[1:].split('@')[0].strip())
        inches_from_left = int(line.split('@')[1].split(',')[0].strip())
        inches_from_top = int(line.split(',')[1].split(':')[0])
        rect_width = int(line.split(':')[1].split('x')[0].strip())
        rect_height = int(line.split('x')[1].strip())

        # Increment the correct parts of the grid for the line.
        for x in range(inches_from_left, inches_from_left + rect_width):
            for y in range(inches_from_top, inches_from_top + rect_height):
                if grid[(x, y)] == 0:
                    grid[(x, y)] = ID
                else:
                    grid[(x, y)] = -1

    return grid


def puzzle1():
    grid = fillGrid()

    # Count the number of overlaps.
    count = 0
    for key, value in grid.items():
        if value == -1:
            count += 1

    return count


def puzzle2():
    lines = open('../Input/input_day3.txt', 'r').readlines()

    grid = fillGrid()

    noOverlapFound = False
    foundID = 0
    while not noOverlapFound:
        for key, value in grid.items():
            if grid[key] > 0:
                ID = grid[key]
                try:
                    for i, line in enumerate(lines):
                        if i == ID - 1:
                            print(f'Checking ID: {ID}')

                            inches_from_left = int(line.split('@')[1].split(',')[0].strip())
                            inches_from_top = int(line.split(',')[1].split(':')[0])
                            rect_width = int(line.split(':')[1].split('x')[0].strip())
                            rect_height = int(line.split('x')[1].strip())

                            # Increment the correct parts of the grid for the line.
                            for x in range(inches_from_left, inches_from_left + rect_width):
                                for y in range(inches_from_top, inches_from_top + rect_height):
                                    print(f'X: {x} - Y: {y} - Value: {grid[(x, y)]}')
                                    if grid[(x, y)] <= 0:
                                        raise OverlapException
                            foundID = ID
                            noOverlapFound = True
                except OverlapException:
                    continue

    return foundID


class OverlapException(Exception):
    pass


print(f'Puzzle 1 outcome: {puzzle1()}')
print(f'Puzzle 2 outcome: {puzzle2()}')
