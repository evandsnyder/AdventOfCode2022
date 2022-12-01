def read_input():
    with open('input/input_day_one.txt', 'r') as f:
        data = f.readlines()

    return data

def part_one():
    file_data = read_input()
    current_calorie_count = 0
    max_calorie = 0

    for line in file_data:
        if line == '\n':
            max_calorie = max(current_calorie_count, max_calorie)
            current_calorie_count = 0
            continue
        current_calorie_count += int(line)
    
    print(f'Part One: {max_calorie}')

def part_two():
    file_data = read_input()
    result = 0

    current_elf = 0
    all_elves = []

    for line in file_data:
        if line == '\n':
            all_elves.append(current_elf)
            current_elf = 0
            continue
        current_elf += int(line)

    # Find the top three largest...
    all_elves.sort(reverse=True)

    print(f'Part Two: {sum(all_elves[:3])}')

def main():
    part_one()
    part_two()

if __name__ == '__main__':
    main()