from problems.problem import Problem


class FileSystemNode:
    def __init__(self, file_name: str, size = 0, is_directory = False, parent = None):
        self.is_directory: bool = is_directory
        self.size: int = size
        self.name: str = file_name
        self.contents: dict[FileSystemNode] | None = {} if self.is_directory else None
        self.parent = parent
        self.is_eligible = False
    
    def __lt__(self, other):
        return self.size < other.size

class DaySeven(Problem):
    def __init__(self, filename, debug):
        super().__init__(filename, debug)

    def read_input(self):
        with open(self.filename, 'r') as f:
            data = f.read().splitlines()

        return data

    def part_one(self):
        self.file_system: FileSystemNode = FileSystemNode("/", size=0, is_directory=True, parent=None)
        current_node = self.file_system
        data = self.read_input()

        while len(data) > 0:
            line = data[0]
            # print(f'Processing line: {line}')
            if line.startswith('$ cd '):
                # command
                line = line.split(' ')
                target_directory = line[-1]
                if target_directory == '..':
                    # move up a directory
                    if current_node.parent != None:
                        # print(f'moving to parent directory: {current_node.parent.name}')
                        current_node = current_node.parent
                elif target_directory == '/':
                    # print('Returning to root')
                    current_node = self.file_system
                else:
                    # from current, move to child directory
                    # print(f'Moving to directory: {target_directory}')
                    if target_directory not in current_node.contents:
                        print('Encountered directory before listing...')
                        # we need to create a new entity for this.. will this happen??
                    current_node = current_node.contents[target_directory]
            elif not line.startswith('$'):
                line = line.split(' ')

                if line[1] in current_node.contents:
                    print("------------------- We've seen this before!!!--------")
                elif line[0] == 'dir':
                    current_node.contents[line[1]] = FileSystemNode(line[1], parent=current_node, is_directory=True)
                else:
                    current_node.contents[line[1]] = FileSystemNode(line[1], size=int(line[0]), parent=current_node)
            data.pop(0)
        
        # file system is built..
        # time to populate the sizes of the entire thing...
        self.build_file_system(self.file_system)
        
        self.print_file_system(self.file_system)

        result: int = 0

        # iterate over all directories and add file_size
        queue: list = [self.file_system]
        while len(queue) > 0:
            directory = queue[0]
            if directory.is_eligible:
                result += directory.size
            
            for node in directory.contents.values():
                if node.is_directory:
                    queue.append(node)
                
            queue.pop(0)
        
        print(f'Part One: {result}')

    def part_two(self):
        total_space = 70000000
        used_space = self.file_system.size
        available_space = total_space - used_space

        required_space = 30000000
        minimum_target_directory_size = required_space - available_space

        # Find all directories larger than minimum_target_directory_size and select smallest..
        eligible_dirs = []
        queue: list[FileSystemNode] = [self.file_system]
        while len(queue) > 0:
            candidate = queue[0]
            if candidate.size >= minimum_target_directory_size:
                eligible_dirs.append(candidate)
            for child in candidate.contents.values():
                if child.is_directory:
                    queue.append(child)
            queue.pop(0)

        print(f'Part Two: {min(eligible_dirs).size}')
    
    def build_file_system(self, file_system: FileSystemNode):
        for node in file_system.contents.values():
            if node.is_directory:
                self.build_file_system(node)
            file_system.size += node.size
        if file_system.is_directory:
            file_system.is_eligible = file_system.size <= 100_000
    
    def print_file_system(self, file_system: FileSystemNode, depth: int = 0):
        prefix = ("  " * depth) + "- "
        print(f"{prefix}{file_system.name} ({'dir' if file_system.is_directory else 'file'}, size={file_system.size})")
        if file_system.is_directory:
            for child in file_system.contents.values():
                self.print_file_system(child, depth + 1)