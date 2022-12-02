from string import Template

word_map = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    21: 'twenty_one',
    22: 'twenty_two',
    23: 'twenty_three',
    24: 'twenty_four',
    25: 'twenty_five'
}

def main():
    with open('utils/problem_tmpl.txt', 'r') as f:
        template = Template(f.read())
    
    for i in range(3, 26):
        # convert i to word..
        day: str = word_map[i]
        filename: str = f"problems/day_{day}.py"

        final_class_name: str = day.capitalize()
        if '_' in final_class_name:
            idx = final_class_name.index('_')
            final_class_name = final_class_name[:idx] + day[idx+1:].capitalize()

        with open(filename, 'w+') as problem_file:
            problem_file.write(template.substitute(className = final_class_name))

        print(f'from .day_{day} import Day{final_class_name}')

if __name__ == '__main__':
    main()