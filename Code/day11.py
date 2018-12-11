def createGrid(serial_number):
    grid = []

    for y in range(1, 301):
        row = []
        [row.append(int(str(((x + 10) * y + serial_number) * (x + 10))[-3]) - 5) for x in range(1, 301)]
        grid.append(row)

    return grid


def puzzle1():
    serial_number = 5177
    grid = createGrid(serial_number=serial_number)

    max_power = [0, 0, 0]
    for i, row in enumerate(grid):
        for j, x in enumerate(row):
            try:
                total_power = 0
                for ix in range(3):
                    for iy in range(3):
                        total_power += grid[i + 1 * ix][j + 1 * iy]

                if total_power > max_power[0]:
                    max_power = [total_power, i, j]
            except IndexError:
                {}

    return f'{max_power[2] + 1}, {max_power[1] + 1}'


def puzzle2():
    serial_number = 5177
    grid = createGrid(serial_number=serial_number)

    max_power = [0, 0, 0, 0]
    for i in range(300):
        for j in range(200, 250):
            try:
                for size in range(5, 20):
                    total_power = 0

                    for ix in range(size):
                        for iy in range(size):
                            total_power += grid[i + 1 * ix][j + 1 * iy]

                    if total_power > max_power[0]:
                        max_power = [total_power, i, j, size]
                        print(f'New max: {max_power}')
            except IndexError:
                {}

    return f'{max_power[2] + 1},{max_power[1] + 1},{max_power[3]}'


print(f'Puzzle 1 outcome: {puzzle1()}')
print(f'Puzzle 2 outcome: {puzzle2()}')
