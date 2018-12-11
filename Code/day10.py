import re
import collections


def determineSecond(points):
    density = 999999
    second = 0
    for i in range(12500):
        min_x = min([x + i * vel_x for [x, y, vel_x, vel_y] in points])
        max_x = max([x + i * vel_x for [x, y, vel_x, vel_y] in points])
        min_y = min([y + i * vel_y for [x, y, vel_x, vel_y] in points])
        max_y = max([y + i * vel_y for [x, y, vel_x, vel_y] in points])

        d = max_x - min_x + max_y - min_y
        if d < density:
            density = d
            second = i

    return second


def drawGrid(max_x, max_y, points):
    # Place the points on the grid.
    for y in range(max_y):
        row = []
        for x in range(max_x):
            char = '.'
            for p in points:
                if p.x == x and p.y == y:
                    char = '@'
                elif p.x > max_x or p.y > max_y:
                    raise IndexError
            row.append(char)
        print(row)


def puzzle1():
    file_input = open('../Input/input_day10.txt', 'r')
    test_input = ['position=< 9,  1> velocity=< 0,  2>', 'position=< 7,  0> velocity=<-1,  0>',
                  'position=< 3, -2> velocity=<-1,  1>', 'position=< 6, 10> velocity=<-2, -1>',
                  'position=< 2, -4> velocity=< 2,  2>', 'position=<-6, 10> velocity=< 2, -2>',
                  'position=< 1,  8> velocity=< 1, -1>', 'position=< 1,  7> velocity=< 1,  0>',
                  'position=<-3, 11> velocity=< 1, -2>', 'position=< 7,  6> velocity=<-1, -1>',
                  'position=<-2,  3> velocity=< 1,  0>', 'position=<-4,  3> velocity=< 2,  0>',
                  'position=<10, -3> velocity=<-1,  1>', 'position=< 5, 11> velocity=< 1, -2>',
                  'position=< 4,  7> velocity=< 0, -1>', 'position=< 8, -2> velocity=< 0,  1>',
                  'position=<15,  0> velocity=<-2,  0>', 'position=< 1,  6> velocity=< 1,  0>',
                  'position=< 8,  9> velocity=< 0, -1>', 'position=< 3,  3> velocity=<-1,  1>',
                  'position=< 0,  5> velocity=< 0, -1>', 'position=<-2,  2> velocity=< 2,  0>',
                  'position=< 5, -2> velocity=< 1,  2>', 'position=< 1,  4> velocity=< 2,  1>',
                  'position=<-2,  7> velocity=< 2, -2>', 'position=< 3,  6> velocity=<-1, -1>',
                  'position=< 5,  0> velocity=< 1,  0>', 'position=<-6,  0> velocity=< 2,  0>',
                  'position=< 5,  9> velocity=< 1, -2>', 'position=<14,  7> velocity=<-2,  0>',
                  'position=<-3,  6> velocity=< 2, -1>']

    # points = [[int(i) for i in re.findall(r'-*\d+', line.rstrip())] for line in test_input]
    points = [[int(i) for i in re.findall(r'-*\d+', line.rstrip())] for line in file_input.readlines()]

    # Find the second where all characters are the closest together.
    second = determineSecond(points)

    # Print that second to figure out the message.
    output = [[' '] * 200 for j in range(400)]
    for (x, y, vx, vy) in points:
        output[y + second * vy + 241][x + second * vx - 310] = '@'

    for o in output:
        print(o)

    return second


def puzzle2():
    file_input = open('../Input/input_day10.txt', 'r')
    test_input = ['position=< 9,  1> velocity=< 0,  2>', 'position=< 7,  0> velocity=<-1,  0>',
                  'position=< 3, -2> velocity=<-1,  1>', 'position=< 6, 10> velocity=<-2, -1>',
                  'position=< 2, -4> velocity=< 2,  2>', 'position=<-6, 10> velocity=< 2, -2>',
                  'position=< 1,  8> velocity=< 1, -1>', 'position=< 1,  7> velocity=< 1,  0>',
                  'position=<-3, 11> velocity=< 1, -2>', 'position=< 7,  6> velocity=<-1, -1>',
                  'position=<-2,  3> velocity=< 1,  0>', 'position=<-4,  3> velocity=< 2,  0>',
                  'position=<10, -3> velocity=<-1,  1>', 'position=< 5, 11> velocity=< 1, -2>',
                  'position=< 4,  7> velocity=< 0, -1>', 'position=< 8, -2> velocity=< 0,  1>',
                  'position=<15,  0> velocity=<-2,  0>', 'position=< 1,  6> velocity=< 1,  0>',
                  'position=< 8,  9> velocity=< 0, -1>', 'position=< 3,  3> velocity=<-1,  1>',
                  'position=< 0,  5> velocity=< 0, -1>', 'position=<-2,  2> velocity=< 2,  0>',
                  'position=< 5, -2> velocity=< 1,  2>', 'position=< 1,  4> velocity=< 2,  1>',
                  'position=<-2,  7> velocity=< 2, -2>', 'position=< 3,  6> velocity=<-1, -1>',
                  'position=< 5,  0> velocity=< 1,  0>', 'position=<-6,  0> velocity=< 2,  0>',
                  'position=< 5,  9> velocity=< 1, -2>', 'position=<14,  7> velocity=<-2,  0>',
                  'position=<-3,  6> velocity=< 2, -1>']

    # points = [[int(i) for i in re.findall(r'-*\d+', line.rstrip())] for line in test_input]
    points = [[int(i) for i in re.findall(r'-*\d+', line.rstrip())] for line in file_input.readlines()]

    # Find the second where all characters are the closest together.
    second = determineSecond(points)

    return second


print(f'Puzzle 1 outcome: {puzzle1()}')
print(f'Puzzle 2 outcome: {puzzle2()}')
