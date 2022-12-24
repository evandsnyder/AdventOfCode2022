from problems.problem import Problem
import functools


class DayThirteen(Problem):
    def __init__(self, filename, debug):
        super().__init__(filename, debug)
        self.read_input()

    def read_input(self):
        with open(self.filename, 'r') as f:
            data = f.read().split('\n\n')
        
        self.packets = []
        for set_data in data:
            self.packets.append(set_data.split('\n'))

    def part_one(self):
        result = 0
        for i in range(len(self.packets)):
            self.debug(f'== Pair {i+1} ==')
            if self.is_in_order(self.packets[i]) > 0:
                result += i+1
        print(f'Part One: {result}')

    def part_two(self):
        # build a list of parsed packets and add dividers...
        all_packets = []
        for packet in self.packets:
            all_packets.append(self.build_list(packet[0][1:-1]))
            all_packets.append(self.build_list(packet[1][1:-1]))
        
        all_packets.append([[2]])
        all_packets.append([[6]])

        # Using the compare function defined below, sort the packets...
        all_packets = sorted(all_packets, key=functools.cmp_to_key(lambda a, b: self.compare(a,b)), reverse=True)

        # find index of [[2]] and [[6]]
        two = 0
        six = 0
        for i in range(len(all_packets)):
            print(all_packets[i])
            if all_packets[i] == [[2]]:
                two = i+1
            if all_packets[i] == [[6]]:
                six = i+1
        
        self.debug(f"TWO: {two}\tSIX: {six}")
        print(f'Part Two: {two*six}')
    
    def is_in_order(self, packet_set: list[str]) -> int:
        left = self.build_list(packet_set[0][1:-1])
        right = self.build_list(packet_set[1][1:-1])

        return self.compare(left, right)
    
    def compare(self, left, right, depth = 0) -> int:
        self.debug(f'{"  "*depth}- Compare {left} vs {right}')

        if isinstance(left, int) and isinstance(right, int):
            if left == right:
                return 0
            r = left < right
            if r:
                self.debug(f'{" "*(depth+2)}- Left side is smaller, so inputs are in the right order')
                return 1
            else:
                self.debug(f'{" "*(depth+2)}- Left side is larger, so inputs are NOT in the right order')
                return -1
        
        if isinstance(left, list) and isinstance(right, list):
            # iterate through each??
            i = 0
            left_len = len(left)
            right_len = len(right)
            t = 0
            while t == 0 and i < left_len and i < right_len:
                t = self.compare(left[i], right[i], depth + 1)
                i += 1

            # if left ran out first, we're good
            if t != 0:
                return t

            if left_len == right_len:
                # Inconclusive???
                return 0
            
            if i == left_len:
                self.debug(f'{" "*(depth+3)}- Left side ran out of items, so inputs are in the right order')
                return 1
            if i == right_len:
                self.debug(f'{" "*(depth+3)}- Right side ran out of items, so inputs are NOT in the right order')
                return -1
            return t

        
        if isinstance(left, int):
            left = [left]
        else:
            right = [right]
        
        return self.compare(left, right, depth + 1)
    
    def build_list(self, raw_packet: str)-> list[list|int]:
        # if first token is not a '[', we can seek till a ','
        # else we need to find the end of the list...
        result = []
        while len(raw_packet):
            if raw_packet[0] == '[':
                seeker = 1
                depth = 1
                while depth > 0 and seeker < len(raw_packet):
                    if raw_packet[seeker] == ']':
                        depth -= 1
                    elif raw_packet[seeker] == '[':
                        depth += 1
                    seeker += 1
                result.append(self.build_list(raw_packet[1:seeker-1]))
                raw_packet = raw_packet[seeker+1:]
            else:
                try:
                    i = raw_packet.index(',')
                    result.append(int(raw_packet[:i]))
                    raw_packet = raw_packet[i+1:]
                except ValueError:
                    result.append(int(raw_packet))
                    raw_packet = ''
        return result