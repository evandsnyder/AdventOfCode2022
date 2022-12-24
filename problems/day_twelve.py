from problems.problem import Problem
import heapq

"""
This is extremely slow for part two... need to figure out how to make it faster...
"""


class Node():
    def __init__(self, char: str, x: int, y: int):
        if char == 'E':
            self.value = 25
        elif char == 'S':
            self.value = 0
        else:
            self.value = ord(char) - 97

        self.x = x
        self.y = y
        self.char = char
        self.visited = False
        self.neighbors = []
        self.distance = 100_000
    
    def print_neighbors(self):
        print(self.neighbors)
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __repr__(self):
        return str(self)
    
    def __str__(self) -> str:
        return f'Node({self.char}, {self.value}, {self.distance}) [{self.x}][{self.y}]'
class DayTwelve(Problem):
    VISITED = 100_000

    def __init__(self, filename, debug):
        super().__init__(filename, debug)
        self.start = Node('a',0,0)
        self.end = Node('z',0,0)
        self.read_input()

    def read_input(self):
        with open(self.filename, 'r') as f:
            data = f.read().splitlines()
        
        self.graph = []
        for x in range(len(data)):
            t = []
            for y in range(len(data[0])):
                t.append(Node(data[x][y], x, y))
            self.graph.append(t)
                


        for i in range(len(self.graph)):
            for j in range(len(self.graph[0])):
                if self.graph[i][j].char == 'S':
                    self.start = self.graph[i][j]
                    self.start.value = ord('a')- 97
                if self.graph[i][j].char == 'E':
                    self.end = self.graph[i][j]
                    self.end.value = ord('z')-97

                neighbor_coords = [
                    (i - 1, j),
                    (i + 1, j),
                    (i, j - 1),
                    (i, j + 1)
                ]

                for edge in neighbor_coords:
                    if edge[0] >= 0 and edge[0] < len(self.graph) and edge[1] >= 0 and edge[1] < len(self.graph[0]) and self.can_step(self.graph[i][j], self.graph[edge[0]][edge[1]]):
                        self.graph[i][j].neighbors.append(self.graph[edge[0]][edge[1]])
        
        self.flat_graph = []
        for row in self.graph:
            for c in row:
                self.flat_graph.append(c)
            
 
    def part_one(self):
        # Find start node.. where char is s
        start_index: int = 0
        end_index: int = 0

        for i in range(len(self.flat_graph)):
            if self.flat_graph[i].char == 'S':
                start_index = i
            if self.flat_graph[i].char == 'E':
                end_index = i
        self.dijkstra_shortest_path(start_index)
        print(f'Part One: {self.flat_graph[end_index].distance}')

    def part_two(self):
        # Find all potential starting points...
        # for node in self.flat_graph
        # Can I find the indexes of all start positions?
        indexes = []

        end_index = 0
        for i in range(len(self.flat_graph)):
            if self.flat_graph[i].value == 0:
                indexes.append(i)
            if self.flat_graph[i].char == 'E':
                end_index = i

        self.debug(f'Potential starting positions: {len(indexes)}')
        lengths = []
        for index in indexes:
            # print(self.flat_graph[index])

            self.dijkstra_shortest_path(index)
            lengths.append(self.flat_graph[end_index].distance)
        
        print(lengths)
        print(f'Part Two: {min(lengths)}')

    def dijkstra_shortest_path(self,start_index: int):
        # self.debug(f'Start node neighbors: {self.start.neighbors}')
        # self.debug(f'End node neighbors: {self.end.neighbors}')

        for node in self.flat_graph:
            node.visited = False
            node.distance = 100_000
        
        self.flat_graph[start_index].distance = 0

        # self.print_graph(self.flat_graph)
        queue = [(v.distance, v) for v in self.flat_graph]
        heapq.heapify(queue)

        while len(queue):
            node = heapq.heappop(queue)[1]
            node.visited = True

            new_dist = node.distance + 1
            for neighbor in node.neighbors:
                #self.debug(f'Testing neighbor: {neighbor}')

                if new_dist < neighbor.distance:
                    #self.debug(f'We\'ve got a new shorter distance: {new_dist}')
                    neighbor.distance = new_dist
            
            queue = [(v.distance, v) for v in self.flat_graph if not v.visited]
            heapq.heapify(queue)
    
    def can_step(self, a: Node, b: Node):
       # self.debug(f'Comparing {b} <= {a} + 1')
        return b.value <= a.value+1

    
    def print_graph(self, graph):
        for node in graph:
            print(str(node))
            node.print_neighbors()
            
