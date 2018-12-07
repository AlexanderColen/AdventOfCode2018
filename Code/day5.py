import string


def react_units(polymer_units):
    size_before = len(polymer_units)
    try:
        for i, unit in enumerate(polymer_units):
            # Check for same letter.
            if unit.lower() == polymer_units[i+1].lower():
                # Check if it is upper + lower or lower + upper.
                if (unit.isupper() and polymer_units[i+1].islower()) \
                        or (unit.islower() and polymer_units[i+1].isupper()):
                    # Pop the specific units from the list and break out of the for loop.
                    polymer_units.pop(i)
                    polymer_units.pop(i)
    except IndexError:
        {}

    size_after = len(polymer_units)
    size_unchanged = size_before == size_after

    return polymer_units, size_unchanged


def puzzle1():
    polymer_units = list(open('../Input/input_day5.txt', 'r').read().rstrip())

    size_unchanged = False
    while not size_unchanged:
        polymer_units, size_unchanged = react_units(polymer_units)

    return len(polymer_units)


def puzzle2():
    polymer_units = list(open('../Input/input_day5.txt', 'r').read().rstrip())
    # Produce dictionary with every letter in the alphabet.
    alphabet_dictionary = dict.fromkeys(string.ascii_lowercase, 0)

    for key in alphabet_dictionary:
        temp_polymer = polymer_units
        # Remove all the instances of this key for the temporary polymer.
        temp_polymer = [x for x in temp_polymer if x != key.lower()]
        temp_polymer = [x for x in temp_polymer if x != key.upper()]

        size_unchanged = False
        while not size_unchanged:
            temp_polymer, size_unchanged = react_units(temp_polymer)

        alphabet_dictionary[key] = len(temp_polymer)
        print(alphabet_dictionary)

    return alphabet_dictionary[min(alphabet_dictionary, key=alphabet_dictionary.get)]


print(f'Puzzle 1 outcome: {puzzle1()}')
print(f'Puzzle 2 outcome: {puzzle2()}')
