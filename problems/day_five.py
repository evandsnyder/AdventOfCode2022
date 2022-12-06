from problems.problem import Problem


class DayFive(Problem):
    file_data: list[str] = []
    towers: list[list] = []
    instructions: list[str] = []

    def __init__(self, filename, debug):
        super().__init__(filename, debug)

    def read_input(self)-> list[str]:
        with open(self.filename, 'r') as f:
            self.file_data = f.read().splitlines()

        return self.file_data

    def part_one(self):
        self.read_input()
        self.create_stacks()

        for inst in self.instructions:
            parts = inst.split()
            count = int(parts[1])
            start = int(parts[3]) - 1
            end = int(parts[5]) - 1

            while len(self.towers[start]) > 0 and count > 0:
                self.towers[end].append(self.towers[start].pop())
                count -= 1

            self.debug(f'Moving {count} from {start} to {end}')
        

        print(f'Part One: {self.get_solution()}')

    def part_two(self):
        # maintain the same order now when moving multiple crates...

        # Rebuilding for a fresh start...
        self.create_stacks()
        for inst in self.instructions:
            parts = inst.split()
            count = int(parts[1])
            start = int(parts[3]) - 1
            end = int(parts[5]) - 1

            move_stack: list[str] = []
            while len(self.towers[start]) > 0 and count > 0:
                move_stack.append(self.towers[start].pop())
                count -= 1
            
            while len(move_stack) > 0:
                self.towers[end].append(move_stack.pop())

        print(f'Part Two: {self.get_solution()}')

    def create_stacks(self):
        tower_entries: list[str] = []
        # iterate until empty line....
        i = 0
        while self.file_data[i] != '':
            self.debug(f'{i}')
            tower_entries.append(self.file_data[i])
            i += 1
        
        i += 1

        tower_count = int(tower_entries[-1].rstrip()[-1])
        tower_entries = tower_entries[:-1]
        self.debug(self.file_data[i])
        self.debug(f'Tower count: {tower_count}')

        self.instructions = self.file_data[i:]

        self.towers: list[list] = [] 

        # Create each tower that we need...
        for i in range(tower_count):
            self.towers.append([])

        # iterate in reverse through all possible towers and add them to the relevant stack...
        for row in reversed(tower_entries):
            row = row.rstrip()
            for j in range(0, len(row), 4):
                if row[j + 1] != ' ':
                    self.towers[j // 4].append(row[j+1])
                    self.debug(f'{row[j+1]}: {j}')
        self.print_towers()
        
    def print_towers(self):
        for tower in self.towers:
            self.debug(''.join(tower))
        
    def get_solution(self) -> str:
        sol = ''
        for tower in self.towers:
            sol += tower[-1]
        return sol
