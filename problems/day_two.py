from enum import IntEnum
from problems.problem import Problem


class Hand(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __str__(self):
        if self.value == 1: return 'ROCK'
        if self.value == 2: return 'PAPER'
        return 'SCISSORS'


class Modifier(IntEnum):
    LOSS = 0
    DRAW = 3
    WIN = 6

    def __str__(self):
        if self.value == 0: return 'LOSS'
        if self.value == 3: return 'DRAW'
        return 'WIN'


class DayTwo(Problem):
    hand_map = {
        'A': Hand.ROCK,
        'B': Hand.PAPER,
        'C': Hand.SCISSORS,
        'X': Hand.ROCK,
        'Y': Hand.PAPER,
        'Z': Hand.SCISSORS
    }

    state_map = {
        'X': Modifier.LOSS,
        'Y': Modifier.DRAW,
        'Z': Modifier.WIN
    }

    win_map = {
        Hand.ROCK: Hand.PAPER,
        Hand.PAPER: Hand.SCISSORS,
        Hand.SCISSORS: Hand.ROCK
    }

    loss_map = {
        Hand.ROCK: Hand.SCISSORS,
        Hand.PAPER: Hand.ROCK,
        Hand.SCISSORS: Hand.PAPER
    }

    def __init__(self, filename, debug):
        super().__init__(filename, debug)

    def read_input(self):
        with open(self.filename, "r") as f:
            data = f.readlines()

        return data

    def part_one(self):
        total_score = 0
        for round in self.read_input():
            if self.DEBUG:
                print(f'RAW HAND: {round[0]} vs {round[2]}')

            total_score += self.calculate_score(self.hand_map[round[0]], self.hand_map[round[2]])

        print(f"Part One: {total_score}")

    def part_two(self):
        total_score = 0

        for round in self.read_input():
            if self.DEBUG:
                print(f'RAW HAND: {round[0]} vs {round[2]}')
            
            # Calculate the new score
            end_state = self.state_map[round[2]]
            opponent = self.hand_map[round[0]]

            total_score += self.calculate_score(opponent, self.pick_player_hand(opponent, end_state))

        print(f"Part Two: {total_score}")

    def calculate_score(self, opponent_hand: Hand, player_hand: Hand) -> int:
        # Figure out which modifier to apply?
        modifier = self.evaluate_round(opponent_hand, player_hand)

        if self.DEBUG:
            print(f'{opponent_hand} vs. {player_hand}')
            print(f'The round was a {modifier}')

        return player_hand + modifier

    
    def pick_player_hand(self, opponent: Hand, target_state: Modifier) -> Hand:
        if target_state == Modifier.DRAW: return opponent

        if target_state == Modifier.WIN:
            return self.win_map[opponent]
        
        return self.loss_map[opponent]

    def evaluate_round(self, opponent: Hand, player: Hand) -> Modifier:
        if opponent == player:
            return Modifier.DRAW

        if player == self.win_map[opponent]:
            return Modifier.WIN

        return Modifier.LOSS