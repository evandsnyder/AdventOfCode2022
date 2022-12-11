from problems.problem import Problem
from math import lcm

class Monkey:
    def __init__(self, data: str):

        lines = data.split('\n')
        self.inventory: list[int] = [int(x) for x in lines[1][lines[1].index(':')+1:].split(', ')]
        self.op: str = lines[2][lines[2].index('=')+1:]
        self.test_val = int(lines[3].split(' ')[-1])

        self.true_case = int(lines[4].split(' ')[-1])
        self.false_case = int(lines[5].split(' ')[-1])

        self.inspection_count = 0

    def eval_round(self, worry_level = 1, multiple: int|None = None) -> tuple:
        self.inspection_count += 1
        old = self.inventory[0]
        new = int(eval(self.op)) // worry_level
        self.inventory.pop(0)

        if multiple:
            new %= multiple

        return new, self.true_case if new % self.test_val == 0 else self.false_case
    
    def __str__(self):
        return f'{self.inspection_count}, {self.inventory}, {self.op}, Test: {self.test_val}, To: [{self.true_case}, {self.false_case}]'


class DayEleven(Problem):
    def __init__(self, filename, debug):
        super().__init__(filename, debug)
        self.monkeys: list[Monkey] = []


    def read_input(self):
        self.monkeys = []
        with open(self.filename, 'r') as f:
            data = f.read()
        
        data = data.split('\n\n')
        for e in data:
            self.monkeys.append(Monkey(e))

    def part_one(self):
        print(f'Part One: {self.simulate(20, worry_level=3)}')
    
    def print_round(self, round: int):
        self.debug(f'After round: {round + 1}, the monkeys are holding items with these worry levels:')
        for i in range(len(self.monkeys)):
            print(f'Monkey {i}: {self.monkeys[i].inventory}')

    def part_two(self):
        print(f'Part Two: {self.simulate(10_000, multiple=True)}')
    
    def simulate(self, rounds: int, worry_level: int = 1, multiple: bool = False):
        self.read_input()

        m = lcm(*[monkey.test_val for monkey in self.monkeys])

        for i in range(rounds):
            for monkey in self.monkeys:
                while len(monkey.inventory) > 0:
                    worry, destination_monkey = monkey.eval_round(worry_level,  multiple=(m if multiple else None))
                    # self.debug(f'Throwing item with worry {worry} to monkey {destination_monkey}')
                    self.monkeys[destination_monkey].inventory.append(worry)
            # self.print_round(i)
        
        vals = [m.inspection_count for m in self.monkeys]
        vals = sorted(vals)
        
        return vals[-1] * vals[-2]
