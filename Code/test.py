import re
from collections import deque


def playGame(last_marble, number_of_players):
    """
    ============================================= GAME RULES ============================================
    - Start with marble 0 in play.
    - Marbles get placed one by one in order from marble 1 until highest marked marble.
    - Game ends when the last marble is placed.
    - Player with highest score at the end wins.
    - Marble that was last placed is the current marble.
    - Marble gets placed between the marble that is 1 right and 2 right of the last current marble
        - If there is no more right, start over from the beginning. (Circle)
    - If marble is a multiple of 23:
        - Marble doesn't get placed but instead gets added to the player's score.
        - The marble 7 left of current marble gets removed and also added to the player's score.
        - Marble 1 right of the previously removed marble becomes the current_marble.
    """
    marbles = deque([0])
    players = [Player(ID=i) for i in range(1, number_of_players + 1)]
    for x in range(1, last_marble):
        if x % 23 != 0:
            marbles.rotate(-1)
            marbles.append(x)
        else:
            marbles.rotate(7)
            players[x % number_of_players].score += marbles.pop() + x
            marbles.rotate(-1)

    scores = []
    for p in players:
        scores.append(p.score)
        # print(p)

    return max(scores)


def puzzle1():
    file_input = open('../Input/input_day9.txt', 'r')
    test_input = '13 players; last marble is worth 7999 points: high score is 146373'

    # player_count, final_marble = list(map(int, filter(None, re.split('\D', test_input))))[:2]
    player_count, final_marble = list(map(int, filter(None, re.split('\D', file_input.readline().rstrip()))))[:2]

    return playGame(last_marble=final_marble, number_of_players=player_count)


def puzzle2():
    file_input = open('../Input/input_day9.txt', 'r')
    test_input = '10 players; last marble is worth 1618 points: high score is 8317'

    # player_count, final_marble = list(map(int, filter(None, re.split('\D', test_input))))[:2]
    player_count, final_marble = list(map(int, filter(None, re.split('\D', file_input.readline().rstrip()))))[:2]
    final_marble *= 100

    return playGame(last_marble=final_marble, number_of_players=player_count)


class Player():
    def __init__(self, ID):
        self.ID = ID
        self.score = 0

    def __str__(self):
        return f'Player: {self.ID} - Score: {self.score}'


print(f'Puzzle 1 outcome: {puzzle1()}')
print(f'Puzzle 2 outcome: {puzzle2()}')
