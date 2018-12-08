import re
import operator


def mapSteps(input):
    # Sort the input alphabetically.
    input.sort()
    letters = set()
    for instruction in input:
        matched_letters = list(filter(None, re.split(r'[a-zA-Z]{2,}|\W', instruction)))
        letters.add(matched_letters[0])
        letters.add(matched_letters[1])

    letters = sorted(letters)
    d = dict.fromkeys(letters, Step())

    for letter in letters:
        d[letter] = Step(name=letter)

    for instruction in input:
        matched_letters = list(filter(None, re.split(r'[a-zA-Z]{2,}|\W', instruction)))
        d[matched_letters[1]].queue.append(matched_letters[0])

    return d


def find_possible_steps(steps):
    possible_next = []
    for k in steps:
        if len(steps[k].queue) == 0:
            possible_next.append(steps[k])

    possible_next.sort(key=operator.attrgetter('name'))

    return possible_next


def find_next_step(steps):
    possible_next = find_possible_steps(steps)
    up_next = None

    try:
        up_next = possible_next[0].name
    except IndexError:
        print('No more instructions left!')

    return up_next


def puzzle1():
    file_input = open('../Input/input_day7.txt', 'r')
    test_input = ['Step C must be finished before step A can begin.',
                  'Step C must be finished before step F can begin.',
                  'Step A must be finished before step B can begin.',
                  'Step A must be finished before step D can begin.',
                  'Step B must be finished before step E can begin.',
                  'Step D must be finished before step E can begin.',
                  'Step F must be finished before step E can begin.']

    steps = mapSteps(file_input.readlines())
    order = []
    while len(steps) > 0:
        up_next = find_next_step(steps)
        order.append(up_next)
        del steps[up_next]
        for k in steps:
            if up_next in steps[k].queue:
                steps[k].queue.remove(up_next)
    return ''.join(order)


def puzzle2():
    file_input = open('../Input/input_day7.txt', 'r')
    test_input = ['Step C must be finished before step A can begin.',
                  'Step C must be finished before step F can begin.',
                  'Step A must be finished before step B can begin.',
                  'Step A must be finished before step D can begin.',
                  'Step B must be finished before step E can begin.',
                  'Step D must be finished before step E can begin.',
                  'Step F must be finished before step E can begin.']

    steps = mapSteps(file_input.readlines())
    workers = []

    # Create the workers.
    for x in range(1, 6):
        workers.append(Worker(ID=x))

    seconds = 0
    done_by = 0
    desired_length = len(steps)
    order = []
    while len(order) != desired_length:
        print(f'Second: {seconds} - Steps remaining: {len(steps)} - '
              f'Order length: {len(order)} - Desired length: {desired_length}')
        # Check if all workers are done.
        for w in workers:
            if w.end_time == seconds:
                step = w.working_on
                order.append(step)
                for k in steps:
                    if step in steps[k].queue:
                        steps[k].queue.remove(step)
                # Update time that it will be done.
                if w.end_time > done_by:
                    done_by = w.end_time

        possible_steps = find_possible_steps(steps)
        if len(possible_steps) != 0:
            for step in possible_steps:
                # Assign the task to a worker.
                for w in workers:
                    if w.end_time <= seconds:
                        w.assignStep(step=step.name, start_time=seconds)
                        del steps[step.name]
                        break
        seconds += 1

    return done_by


class Step:
    def __init__(self, name='.', firstQueue=''):
        # Create all variables set them to the parameters.
        self.name = name
        self.queue = []
        self.time_required = 60 + ord(name) - 64
        if firstQueue != '':
            self.queue.append(firstQueue)

    def __str__(self):
        return f'Name: {self.name} - Time Required: {self.time_required} - Blocked By: {self.queue}'


class Worker:
    def __init__(self, ID=0):
        # Create all variables set them to the parameters.
        self.ID = ID
        self.working_on = '.'
        self.start_time = -1
        self.end_time = -1

    def assignStep(self, step, start_time):
        self.working_on = step
        self.start_time = start_time
        self.end_time = start_time + 60 + ord(step) - 64
        print(f'Assigning step {step} to worker {self.ID} at {start_time} until {self.end_time}')

    def __str__(self):
        return f'ID: {self.ID} - Working On: {self.working_on} - ' \
               f'Start Time: {self.start_time} - End Time: {self.end_time}'


print(f'Puzzle 1 outcome: {puzzle1()}')
print(f'Puzzle 2 outcome: {puzzle2()}')
