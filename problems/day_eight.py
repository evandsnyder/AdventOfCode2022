import copy
from problems.problem import Problem


class DayEight(Problem):
    def __init__(self, filename, debug):
        super().__init__(filename, debug)

    def read_input(self):
        with open(self.filename, 'r') as f:
            data = f.read().splitlines()
        
        grid = [[int(x) for x in l] for l in data]

        return grid

    def part_one(self):
        self.height_map = self.read_input()

        # count perimeter trees...
        length = len(self.height_map)
        width = len(self.height_map[0])
        visible_trees = length * 2 + ((width - 2) * 2)

        for i in range(1, len(self.height_map) - 1):
            for j in range(1, len(self.height_map[i]) - 1):
                if self.is_visible(i, j, self.height_map):
                    visible_trees += 1
        
        print(f'Part One: {visible_trees}')

    def part_two(self):
        largest_view_distance = 0
        for i in range(len(self.height_map)):
            for j in range(len(self.height_map[i])):
                largest_view_distance = max(largest_view_distance, self.calculate_view_distance(i, j))
                
        print(f'Part Two: {largest_view_distance}')
    
    def print_grid(self, grid: list[list[int]]) -> None:
        for row in grid:
            r = ''
            for col in row:
                r += f'{col} '
            print(r)
    
    def is_visible(self, row: int, col: int, map: list[list[int]]) -> bool:
        # A tree is visible if it can be seen from up, left, right, or down
        # Start by checking the row it is in...
        # if ever value to the left is less than or every value to the right...
        

        left_side = map[row][:col]
        right_side = map[row][col+1:]

        tree = map[row][col]

        # print(f'------------------ CHECKING FOR {tree} -----------------------')

        can_be_seen_row = max(left_side) < tree or max(right_side) < tree

        # print(left_side)
        # print(right_side)

        col_as_row = [x[col] for x in map]
        # print(col_as_row)
        top = col_as_row[:row]
        bot = col_as_row[row+1:]

        # print(top)
        # print(bot)

        can_be_seen_col= max(top) < tree or max(bot) < tree

        return can_be_seen_row or can_be_seen_col
    
    def calculate_view_distance(self, row: int, col: int) -> int:
        left = 0
        right = 0
        down = 0
        up = 0

        tree = self.height_map[row][col]

        # how far can we see to the left...
        tree_row = self.height_map[row]
        # move from current to left until >=
        i = col - 1
        while i >= 0:
            left += 1
            if tree_row[i] >= tree:
                break
            i -= 1
        # look right..
        i = col + 1
        while i < len(tree_row):
            right += 1
            if tree_row[i] >= tree:
                break
            i += 1

        # Time to look up and down..
        tree_col = [x[col] for x in self.height_map]
        # look up
        i = row - 1
        while i >= 0:
            up += 1
            if tree_col[i] >= tree:
                break
            i -= 1
        
        # look down..
        i = row + 1
        while i < len(tree_col):
            down += 1
            if tree_col[i] >= tree:
                break
            i += 1

        return up * down * left * right