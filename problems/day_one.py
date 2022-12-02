from problems.problem import Problem


class DayOne(Problem):
    def __init__(self, filename, debug):
        super().__init__(filename, debug)

    def read_input(self):
        print(self.filename)
        with open(self.filename, 'r') as f:
            data = f.readlines()

        return data

    def part_one(self):
        file_data = self.read_input()
        current_calorie_count = 0
        max_calorie = 0

        for line in file_data:
            if line == '\n':
                max_calorie = max(current_calorie_count, max_calorie)
                current_calorie_count = 0
                continue
            current_calorie_count += int(line)
        
        print(f'Part One: {max_calorie}')

    def part_two(self):
        file_data = self.read_input()

        current_elf = 0
        all_elves = []

        for line in file_data:
            if line == '\n':
                all_elves.append(current_elf)
                current_elf = 0
                continue
            current_elf += int(line)

        # Find the top three largest...
        all_elves.sort(reverse=True)

        print(f'Part Two: {sum(all_elves[:3])}')