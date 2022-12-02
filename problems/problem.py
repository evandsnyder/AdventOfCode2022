class Problem:
    filename = ''
    DEBUG = False
    def __init__(self, filename, debug):
        self.filename = filename
        self.DEBUG = debug

    def part_one(self):
        raise NotImplementedError()
    
    def part_two(self):
        raise NotImplementedError()
    
    def read_input(self):
        raise NotImplementedError()