from problems.problem import Problem

X = 0
Y = 1

class Coord:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y 

class DayNine(Problem):
    def __init__(self, filename, debug):
        super().__init__(filename, debug)
        self.instructions = self.read_input()

    def read_input(self):
        with open(self.filename, 'r') as f:
            data = f.read().splitlines()

        return data

    def part_one(self):
        knots = [(0,0), (0,0)]
        visited_positions: set = set()

        for line in self.instructions:
            self.process_instruction(visited_positions, line, knots)

        print(f'Part One: {len(visited_positions)}')

    def part_two(self):
        knots: list(tuple) = []
        visited_positions: set = set()

        for _ in range(10):
            knots.append((0,0))
        
        for line in self.instructions:
            self.process_instruction(visited_positions, line, knots)

        print(f'Part Two: {len(visited_positions)}')
    
    def process_instruction(self, positions: set, instruction: str, knots: list[tuple]) -> None:
        instruction = instruction.split(' ')

        if len(instruction) == 0:
            return
        
        direction = instruction[0]
        distance = int(instruction[-1])

        for _ in range(distance):
            # Update head..
            if direction == 'L':
                knots[0] = (
                    knots[0][X] - 1,
                    knots[0][Y]
                )
            elif direction == 'R':
                knots[0] = (
                    knots[0][X] + 1,
                    knots[0][Y]
                )
            elif direction == 'U':
                knots[0] = (
                    knots[0][X],
                    knots[0][Y] + 1
                )
            else:
                knots[0] = (
                    knots[0][X],
                    knots[0][Y] - 1
                )

            # We need to update the ret of the children now...
            for i in range(1, len(knots)):
                if not self.is_touching(knots[i-1], knots[i]):
                    # Update the child!
                    self.move_knot(knots, i)

            positions.add(knots[-1])
    
    def is_touching(self, knot1: tuple, knot2: tuple) -> bool:
        potential_neighbors = [
            (knot1[X]-1, knot1[Y]+1),
            (knot1[X], knot1[Y]+1),
            (knot1[X]+1, knot1[Y]+1),
            (knot1[X]-1, knot1[Y]),
            (knot1[X], knot1[Y]),
            (knot1[X]+1, knot1[Y]),
            (knot1[X]-1, knot1[Y]-1),
            (knot1[X], knot1[Y]-1),
            (knot1[X]+1, knot1[Y]-1)
        ]
        return knot2 in potential_neighbors

    def move_knot(self, knots: list[tuple], i: int):
        if knots[i-1][Y] == knots[i][Y]:
            # must be horizontal only!
            knots[i] = (
                knots[i][X] + (1 if knots[i-1][X] > knots[i][X] else -1),
                knots[i][Y]
            )
        elif knots[i-1][X] == knots[i][X]:
            # must be vertical only!
            knots[i] = (
                knots[i][X],
                knots[i][Y] + (1 if knots[i-1][Y] > knots[i][Y] else -1)
            )
            
        else:
            if knots[i-1][Y] == knots[i][Y] + 2:
                knots[i] = (
                    knots[i][X] + (1 if knots[i-1][X] > knots[i][X] else -1),
                    knots[i][Y] + 1
                )
            elif knots[i-1][Y] == knots[i][Y] - 2:
                # down
                knots[i] = (
                    knots[i][X] + (1 if knots[i-1][X] > knots[i][X] else -1),
                    knots[i][Y] - 1
                )
            elif knots[i-1][X] == knots[i][X] - 2:
                # left
                knots[i] = (
                    knots[i][X] - 1,
                    knots[i][Y] + (1 if knots[i-1][Y] > knots[i][Y] else -1)
                )
            elif knots[i-1][X] == knots[i][X] + 2:
                knots[i] = (
                    knots[i][X] + 1,
                    knots[i][Y] + (1 if knots[i-1][Y] > knots[i][Y] else -1)
                )    
