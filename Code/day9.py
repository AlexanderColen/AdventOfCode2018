import re


def assignMarbles(puzzle_input):
    number_of_players, last_marble = list(map(int, filter(None, re.split('\D', puzzle_input))))[:2]
    players = []
    for x in range(1, number_of_players + 1):
        players.append(Player(ID=x))

    for marble in range(1, last_marble + 1):
        players[(marble % number_of_players) - 1].marbles.append(marble)

    return players, last_marble


def determine_place_index(placed_marbles, current_marble, marble):
    current_index = placed_marbles.index(current_marble)
    new_index = current_index + 2
    if new_index > len(placed_marbles):
        new_index = new_index - len(placed_marbles)

    return new_index


def puzzle1():
    file_input = open('../Input/input_day9.txt', 'r')
    test_input = '13 players; last marble is worth 7999 points: high score is 146373'

    players, last_marble = assignMarbles(file_input.readline().rstrip())
    # players, last_marble = assignMarbles(puzzle_input=test_input)

    """
    ========== GAME RULES ==========
    - Start with marble 0 (current_marble == 0)
    - Marbles get placed one by one in order from marble 1 until highest marked marble.
    - Game ends when the last marble is placed.
    - Player with highest score at the end wins.
    - Marble that was last placed is the current marble AFTER IT IS PLACED.
    - Marble gets placed between the marble that is 1 right and 2 right of the last current marble
        - If there is no more right, start over from the beginning. (CIRCLE) 
    - If marble is a multiple of 23 (% 23 == 0):
        - Marble doesn't get placed but instead gets added to the player's score.
        - The marble 7 left of current marble gets removed and also added to the player's score.
        - Marble 1 right of the previously removed marble becomes the current_marble.
    """

    turn = 0
    current_marble = 0
    placed_marbles = [0]
    while turn != last_marble:
        current_player = players[turn % len(players)]
        marble = current_player.marbles[0]

        if marble % 23 == 0:
            current_player.score += marble
            current_player.marbles.remove(marble)
            # Marble to be removed is 7 left of current marble.
            removal_index = placed_marbles.index(current_marble) - 7
            # If the index is below 0, count the negative amount back from the end.
            if removal_index < 0:
                # Save what marble needs to be removed.
                removed_marble = placed_marbles[len(placed_marbles) + removal_index]
                # Add this marble to the player's score.
                current_player.score += removed_marble
                # Remove the marble.
                placed_marbles.remove(removed_marble)
                # Make sure the new current marble's index is not below zero, otherwise count back from end of array.
                # New current marble would be 1 right of the removed marble index = 6 left from the current marble.
                new_current_index = placed_marbles.index(current_marble) - 6
                if new_current_index < 0:
                    current_marble = placed_marbles[len(placed_marbles) + new_current_index]
                else:
                    current_marble = placed_marbles[new_current_index]
            # Else just remove the marble at the removal_index.
            else:
                # Save what marble needs to be removed.
                removed_marble = placed_marbles[removal_index]
                # Add this marble to the player's score.
                current_player.score += removed_marble
                # Remove the marble.
                placed_marbles.remove(removed_marble)
                # New current marble would be 1 right of the removed marble index = 6 left from the current marble.
                current_marble = placed_marbles[placed_marbles.index(current_marble) - 6]
        else:
            place_index = determine_place_index(placed_marbles=placed_marbles,
                                                current_marble=current_marble, marble=marble)
            placed_marbles.insert(place_index, marble)
            current_player.marbles.remove(marble)
            current_marble = marble

        turn += 1
        # print('{:0>5d}'.format(turn) + f' Player: {current_player.ID} - Current Marble: {current_marble} - {placed_marbles}')

    scores = []
    for p in players:
        print(p)
        scores.append(p.score)

    return max(scores)


def puzzle2():
    file_input = open('../Input/input_day9.txt', 'r')
    test_input = []

    return 0


class Player:
    def __init__(self, ID):
        self.ID = ID
        self.marbles = []
        self.score = 0

    def __str__(self):
        return f'Player: {self.ID} - Score: {self.score} - Remaining Marbles: {self.marbles}'


print(f'Puzzle 1 outcome: {puzzle1()}')
print(f'Puzzle 2 outcome: {puzzle2()}')
