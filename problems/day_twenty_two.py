from problems.problem import Problem


class DayTwentyTwo(Problem):
    def __init__(self, filename, debug):
        super().__init__(filename, debug)

    def read_input(self):
        with open(self.filename, 'r') as f:
            data = f.readlines()

        return data

    def part_one(self):
        print(f'Part One: {0}')

    def part_two(self):
        print(f'Part Two: {0}')