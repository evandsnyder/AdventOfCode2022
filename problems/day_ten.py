from problems.problem import Problem


class DayTen(Problem):
    def __init__(self, filename, debug):
        super().__init__(filename, debug)
        self.register_x = 1
        self.cycle = 0
        self.crt = ''

        self.instructions = self.read_input()

    def read_input(self):
        with open(self.filename, 'r') as f:
            data = f.read().splitlines()

        return data

    def part_one(self) -> None:
        signal_strength = 0
        for op in self.instructions:
            self.crt += self.get_pixel()
            self.cycle += 1
            signal_strength += self.get_signal_strength()
            if 'addx' in op:
                self.crt += self.get_pixel()
                self.cycle += 1
                signal_strength += self.get_signal_strength()
                self.register_x += int(op.split()[1])
                self.debug(f'cycle: {self.cycle}, register: {self.register_x}')

        print(f'Part One: {signal_strength}')

    def part_two(self) -> None:
        print(f'Part Two: {self.crt}')

    def get_pixel(self) -> str:
        crt = ''
        cursor = self.cycle % 40
        if cursor == 0:
            crt += '\n'
        
        crt += '#' if cursor in [self.register_x - 1, self.register_x, self.register_x + 1] else '.'

        return crt
    
    def get_signal_strength(self) -> int:
        if self.cycle < 221 and self.cycle % 40 == 20:
            return self.cycle * self.register_x
        return 0