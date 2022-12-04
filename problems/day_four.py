from problems.problem import Problem


class SectorZones:
    def __init__(self, zone_range: str):
        info = zone_range.split('-')
        self.start = int(info[0])
        self.end = int(info[1])


class DayFour(Problem):
    def __init__(self, filename, debug):
        super().__init__(filename, debug)

    def read_input(self):
        with open(self.filename, 'r') as f:
            data = f.read().splitlines()
        return data

    def part_one(self):
        encapsulated_pairs = 0

        pairs = self.read_input()
        for pair in pairs:
            pair = pair.split(',')
            elf_one = SectorZones(pair[0])
            elf_two = SectorZones(pair[1])
            if self.is_encapsulated(elf_one, elf_two):
                encapsulated_pairs += 1

        print(f'Part One: {encapsulated_pairs}')

    def part_two(self):
        overlapping_pairs = 0

        pairs = self.read_input()
        for pair in pairs:
            pair = pair.split(',')
            elf_one = SectorZones(pair[0])
            elf_two = SectorZones(pair[1])
            if self.is_overlapping(elf_one, elf_two) or self.is_overlapping(elf_two, elf_one):
                overlapping_pairs += 1
        print(f'Part Two: {overlapping_pairs}')

    def is_encapsulated(self, elf_one: SectorZones, elf_two: SectorZones) -> bool:
        return (elf_one.start <= elf_two.start and elf_one.end >= elf_two.end) \
            or (elf_two.start <= elf_one.start and elf_two.end >= elf_one.end)

    def is_overlapping(self, elf_one: SectorZones, elf_two: SectorZones) -> bool:
        return (elf_two.start <= elf_one.end and elf_two.end >= elf_one.start) \
            or (elf_one.start <= elf_two.end and elf_one.end >= elf_two.start)