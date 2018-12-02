def puzzle1(frequency=0):
    file_input = open('../Input/input_day1.txt', 'r')
    for line in file_input:
        frequency += int(line)
    return frequency


def puzzle2(frequency=0, old_frequencies=[], count=0):
    count += 1
    file_input = open('../Input/input_day1.txt', 'r')
    for line in file_input:
        frequency += int(line)
        if frequency in old_frequencies:
            return frequency, count
        old_frequencies.append(frequency)
    return puzzle2(frequency=frequency, old_frequencies=old_frequencies, count=count)


print(f'Puzzle 1 output: {puzzle1()}')
puz2_output, times_looped = puzzle2()
print(f'Puzzle 2 output: {puz2_output} (after {times_looped} loops)')
