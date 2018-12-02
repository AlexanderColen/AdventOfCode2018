from collections import Counter


def puzzle1():
    file_input = open('../Input/input_day2.txt', 'r')
    twos = 0
    threes = 0

    for line in file_input:
        found_two = False
        found_three = False

        letters = list(line)
        counter = Counter(letters)

        for key in counter.keys():
            if counter.get(key) == 2 and not found_two:
                twos += 1
                found_two = True
            elif counter.get(key) == 3 and not found_three:
                threes += 1
                found_three = True
    print(twos, threes)
    return twos * threes


def puzzle2():
    file_input = open('../Input/input_day2.txt', 'r')
    file_input_2 = open('../Input/input_day2.txt', 'r')
    lines1 = file_input.readlines()
    lines2 = file_input_2.readlines()

    for line in lines1:
        letters_1 = list(line)
        wanted = len(letters_1) - 1

        for line2 in lines2:
            current = 0
            letters_2 = list(line2)

            for x in range(len(letters_1)):
                if letters_1[x] == letters_2[x]:
                    current += 1
            if current == wanted:
                output = []
                print(line, line2)
                for x in range(len(letters_1)):
                    if letters_1[x] == letters_2[x]:
                        output.append(letters_1[x])
                return ''.join(output)


print(f'Puzzle 1 output: {puzzle1()}')
print(f'Puzzle 2 output: {puzzle2()}')
