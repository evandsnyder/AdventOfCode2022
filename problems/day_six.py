from problems.problem import Problem


class DaySix(Problem):
    def __init__(self, filename, debug):
        super().__init__(filename, debug)

    def read_input(self):
        with open(self.filename, 'r') as f:
            data = f.read().strip()

        return data

    def part_one(self):
        if self.DEBUG:
            self.run_test_cases(4)
            return

        start_of_packet: int = self.find_start_of_sequence(self.read_input(), 4)
        print(f'Part One: {start_of_packet}')

    def part_two(self):
        if self.DEBUG:
            self.run_test_cases(14)
            return

        start_of_message = self.find_start_of_sequence(self.read_input(), 14)
        print(f'Part Two: {start_of_message}')
    
    def is_unique(self, candidate: str) -> bool:
        known_values: set = set()

        for char in candidate:
            if ord(char) in known_values: return False
            known_values.add(ord(char))

        return True
    
    
    def find_start_of_sequence(self, buffer: str, sequence_size: int) -> int:
        i: int = 0
        while i < len(buffer) - sequence_size:
            potential: str = buffer[i:i+sequence_size]
            self.debug(f'Potential sequence: {potential}')
            if self.is_unique(potential):
                break
            i += 1
        return i + sequence_size
    
    def run_test_cases(self, sequence_size) -> None:
        test_cases = ['bvwbjplbgvbhsrlpgdmjqwftvncz', 'nppdvjthqldpwncqszvftbrmjlhg', 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 'mjqjpqmgbljsphdztnvjfqwrcgsmlb']
        test_solutions = [5,6,10,11,7]
        if sequence_size == 14:
            test_solutions = [23, 23, 29, 26, 19]

        for i in range(len(test_cases)):
            self.debug(f'Test case {i+1} {"passed" if self.find_start_of_sequence(test_cases[i], sequence_size) == test_solutions[i] else "failed"}!')
