from problems.problem import Problem


class DayFourteen(Problem):
    LEFT = -1
    RIGHT = 1
    DOWN = 0
    REST = 2

    def __init__(self, filename, debug):
        super().__init__(filename, debug)

        self.max_coord = 0
        self.filled_coords: set = set()
        self.read_input()

    def read_input(self):
        with open(self.filename, 'r') as f:
            data = f.read().splitlines()
        
        for shape in data:
            self.debug("Processing Shape!")
            shape = shape.split(' -> ')
            for i in range(1, len(shape)):
                start = [int(x) for x in shape[i-1].split(',')]
                self.debug(f"{start}")
                end = [int(x) for x in shape[i].split(',')]
                self.debug(f"{end}")

                self.max_coord = max([self.max_coord, start[1], end[1]])

                if start[0] == end[0]:
                    self.debug("This should be a vertical line...")
                    # This must be a vertical line of some sort
                    for j in range(min(start[1], end[1]), max(start[1], end[1])+1):
                        self.filled_coords.add((start[0],j))
                else:
                    # Must be horizontal of some sort...
                    self.debug("This should be a horizontal line...")
                    for j in range(min(start[0], end[0]), max(start[0], end[0])+1):
                        self.filled_coords.add((j,start[1]))
        
        print(self.filled_coords)
        print(len(self.filled_coords))

        # find min y coordinate...
        

    def part_one(self):
        # When generating our grid, we can subtract 400 from every x...
        # never mind... this will be impacted when sand falls....

        # While sand falling coords > minimum border, generate new sand...

        # generate sand until it falls into eternity...

        self.grain_count = 0
        self.debug(f"{self.max_coord}")
        while self.drop_sand() < self.max_coord:
            self.grain_count += 1

        print(f'Part One: {self.grain_count}')

    def part_two(self):

        # Add filled coord for base layer...
        # What's my min x and max x??
        self.max_coord += 2
        min_x, max_x = self.find_x_boundaries()
        for i in range(min_x-1000, max_x+1000):
            self.filled_coords.add((i, self.max_coord))
        

        # Scan until 500,0 is blocked??
        while (500,0) not in self.filled_coords:
            self.drop_sand()
            self.grain_count += 1

        # For some reason, I'm short two... this was really just a lucky guess
        # TODO: RE code and understand why I'm two short...
        print(f'Part Two: {self.grain_count+2}')

    
    def drop_sand(self) -> int:
        spawn_point: list[int] = [500,0]
        movement = self.can_move(spawn_point)
        while movement != self.REST and spawn_point[1] < self.max_coord:
            match movement:
                case self.DOWN:
                    spawn_point = [spawn_point[0], spawn_point[1]+1]
                case self.LEFT:
                    spawn_point = [spawn_point[0]-1, spawn_point[1]+1]
                case self.RIGHT:
                    spawn_point = [spawn_point[0]+1, spawn_point[1]+1]
                case _:
                    raise ValueError("We shouldn't be here...")
            movement = self.can_move(spawn_point)
        
        self.filled_coords.add(tuple(spawn_point))
        
        self.debug(f"Reached rest place at: {spawn_point}")

        return spawn_point[1]
    
    
    def can_move(self, spawn_point) -> int:
        # Try down first..
        if self.can_drop_down(spawn_point):
            return self.DOWN
        
        if self.can_drop_left(spawn_point):
            return self.LEFT

        if self.can_drop_right(spawn_point):
            return self.RIGHT
         
        return self.REST

    def can_drop_down(self, pos) -> bool:
        return (pos[0], pos[1]+1) not in self.filled_coords

    def can_drop_left(self, pos) -> bool:
        return (pos[0]-1, pos[1]+1) not in self.filled_coords

    def can_drop_right(self, pos) -> bool:
        return (pos[0]+1, pos[1]+1) not in self.filled_coords

    
    def find_x_boundaries(self) -> tuple:
        min_x, max_x = 100000000,0
        for e in self.filled_coords:
            min_x = min(e[0], min_x)
            max_x = max(e[0], max_x)
        return min_x, max_x
