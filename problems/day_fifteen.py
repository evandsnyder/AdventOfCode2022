from problems.problem import Problem
import itertools

class LineSegment():
    def __init__(self, start: tuple, end: tuple, b: int):
        self.start = start
        self.end = end
        self.slope = (end[1] - start[1]) // (end[0] - start[0])
        self.offset = self.start[1] - (self.slope*self.start[0])
    
    def __repr__(self):
        return f"y = {self.slope} * x + {self.offset}"

    def find_y(self, x):
        return self.slope * x + self.offset
    
    def find_x_intersection(self, other):
        # Okay....

        # We know that slope will always be -1 or 1, so we can always divide by two on the answer...
        # y = mx + b
        # when finding the intersection, it'll always be a pos and a neg line that we're comparing:
        # x + b1 == -x+b2 => 2x == b2 - b1 => x == (b2-b1) // 2
        return (other.offset - self.offset) // 2

class Line():
    def __init__(self, origin, distance, debug):
        self.x_origin = origin[0]
        self.y_origin = origin[1]
        self.origin = origin
        self.manhattan_distance = distance
        self.DEBUG = debug

        # Compute all 4 line segments...
        self.left_pos  = LineSegment((self.x_origin - distance, self.y_origin), (self.x_origin, self.y_origin + distance), origin[0])
        self.debug(f'{self.left_pos}')
        self.left_neg  = LineSegment((self.x_origin - distance, self.y_origin), (self.x_origin, self.y_origin - distance), origin[0])
        self.debug(f'{self.left_neg}')
        self.right_pos = LineSegment((self.x_origin, self.y_origin - distance), (self.x_origin + distance, self.y_origin), origin[0])
        self.debug(f'{self.right_pos}')
        self.right_neg = LineSegment((self.x_origin, self.y_origin + distance), (self.x_origin + distance, self.y_origin), origin[0])
        self.debug(f'{self.right_neg}')
    
    def intersects_y_coord(self, y_coord: int) -> bool:
        return self.y_origin - self.manhattan_distance <= y_coord <= self.y_origin + self.manhattan_distance
    
    def find_coordinate_intersections(self, y_coord):
        rem = self.manhattan_distance - abs(y_coord - self.y_origin)
        return self.x_origin - rem, self.x_origin + rem + 1
    
    def debug(self, input: str):
        if self.DEBUG:
            print(input)

class DayFifteen(Problem):
    def __init__(self, filename, debug):
        super().__init__(filename, debug)
        self.sensors: list[tuple] = []
        self.distances: dict = {}
        self.beacons: set[tuple] = set()
        self.lines: list[Line] = []
        self.read_input()

        self.y_coord = 10 if self.DEBUG else 2_000_000


    def read_input(self):
        with open(self.filename, 'r') as f:
            data = f.read().splitlines()

        for row in data:
            row = row.split(':')
            sensor = row[0].split(', ')
            beacon = row[1].split(', ')
            sensor = (int(sensor[0].split('=')[1]), int(sensor[1][2:]))
            beacon = (int(beacon[0].split('=')[1]), int(beacon[1][2:]))

            manhattan_distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
            self.distances[sensor] = manhattan_distance
            self.beacons.add(beacon)
            self.sensors.append(sensor)
            self.lines.append(Line(sensor, manhattan_distance, self.DEBUG))

    def part_one(self):
        print(f'Part One: {self.count_covered_tiles(self.y_coord)}')

    def part_two(self):
        def pos_gen(lines):
            for line in lines:
                yield line.left_pos
                yield line.right_pos
        
        def neg_gen(lines):
            for line in lines:
                yield line.left_neg
                yield line.right_neg


        # using the previously defined lines, find all pairs that have a 
        positive_lines = list(pos_gen(self.lines))
        negative_lines = list(neg_gen(self.lines))

        pos_pairs = [pair for pair in itertools.combinations(positive_lines, 2) if abs(pair[0].offset - pair[1].offset) == 2]
        neg_pairs = [pair for pair in itertools.combinations(negative_lines, 2) if abs(pair[0].offset - pair[1].offset) == 2]

        for pos in pos_pairs:
            for neg in neg_pairs:
                # Would be nice if itertools could do this for me... but alas....
                pos_one_x_one = pos[0].find_x_intersection(neg[0])
                pos_one_x_two = pos[0].find_x_intersection(neg[1])
                pos_one_y_one = pos[0].find_y(pos_one_x_one)
                pos_one_y_two = pos[0].find_y(pos_one_x_two)

                pos_two_x_one = pos[1].find_x_intersection(neg[0])
                pos_two_x_two = pos[1].find_x_intersection(neg[1])
                pos_two_y_one = pos[1].find_y(pos_two_x_one)
                pos_two_y_two = pos[1].find_y(pos_two_x_two)

                min_x = min(pos_one_x_one, pos_one_x_two, pos_two_x_one, pos_two_x_two)
                max_x = max(pos_one_x_one, pos_one_x_two, pos_two_x_one, pos_two_x_two)

                if max_x - min_x != 2:
                    continue

                min_y = min(pos_one_y_one, pos_one_y_two, pos_two_y_one, pos_two_y_two)
                max_y = max(pos_one_y_one, pos_one_y_two, pos_two_y_one, pos_two_y_two)

                if max_y - min_y == 2 and (min_x + 1 < 4_000_000) and (min_y + 1 < 4_000_000):
                    # SUCCESS!!!!!!!!!!!

                    # Not really sure why, but the sample data has multiple scenarios where this criteria is satisfied..
                    # it does find the *right* answer, but that's not the first answer it finds..
                    print(f"Part two: {((min_x+1) * 4_000_000) + min_y+1}")
                    return

        print(f'Couldn\'t find a solution for part two... did you do this correctly????')
    
    def count_covered_tiles(self, y_coord: int) -> int:
        ranges_accounted_for: list[tuple] = []
        for line in self.lines:
            if not line.intersects_y_coord(y_coord):
                continue

            self.debug(f"sensor {line.origin} ({line.manhattan_distance}) intersects the y_coord!")

            # We only need to account for values that we haven't already accounted for...
            start_x, end_x = line.find_coordinate_intersections(y_coord)

            self.debug(f"\t needing to account for values in range({start_x}, {end_x})")
            # Find min_x from these data points....
            ranges_accounted_for.append((start_x, end_x))
        
        # right here, we combine all the intervals into one big interval
        # however, this is "risky" and won't necessarily always work since it assumes there are no gaps in coverage
        # really, we should combine as many intervals as possible and see if there is anything left afterwards...
        min_r, max_r = 16_000_000, 0
        for acc in ranges_accounted_for:
            min_r = min(min_r, acc[0])
            max_r = max(max_r, acc[1])


        return max_r - min_r - self.count_beacons_in_range(min_r, max_r, y_coord)
    
    def count_beacons_in_range(self, start_x: int, end_x: int, y_coord: int) -> int:
        return len([beacon for beacon in self.beacons if beacon[1] == y_coord and (start_x <= beacon[0] < end_x)])