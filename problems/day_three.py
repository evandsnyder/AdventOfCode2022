from problems.problem import Problem


class DayThree(Problem):
    def __init__(self, filename, debug):
        super().__init__(filename, debug)

    def read_input(self):
        with open(self.filename, 'r') as f:
            data = f.read().splitlines()

        return data

    def part_one(self) -> None:
        rucksacks: list[str] = self.read_input()
        result: int = 0

        for ruck in rucksacks:
            mid_point: int = len(ruck) // 2
            self.debug(f'midpoint: {mid_point}')
            comp_one: str = ruck[:mid_point]
            comp_two: str = ruck[mid_point:]

            self.debug(f'compartment_one: {comp_one}')
            self.debug(f'compartment_two: {comp_two}')

            # find shared letter between them...
            result += self.find_priority((set(comp_one) & set(comp_two)).pop())
    
        print(f'Part One: {result}')

    def part_two(self) -> None:
        rucks: list[str] = self.read_input()
        result: int = 0 
        
        for i in range(0, len(rucks), 3):
            same_items = set(rucks[i]) & set(rucks[i+1]) & set(rucks[i+2])
            result += self.find_priority(same_items.pop())

        print(f'Part Two: {result}')
    
    def find_priority(self, char: str) -> int:
        priority = ord(char)
        if priority > 96:
            return priority - 96

        return priority - 38