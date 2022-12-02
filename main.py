from problem_factory import ProblemFactory

import argparse

def main():
    parser = argparse.ArgumentParser(
        prog = 'Advent of Code 2022 Driver',
        description= 'Used for running the 2022 Advent of Code problems'
    )

    parser.add_argument('day', nargs='?')
    parser.add_argument('-D', '--debug', action='store_true', default=False)

    args = parser.parse_args()
    factory = ProblemFactory()

    if args.day is None:
        for i in range(1, 26):
            print(f"Running day: {i}")
            problem = factory.build_problem(i, args.debug)
            problem.part_one()
            problem.part_two()
    else:
        print(f"Running day: {args.day}")
        problem = factory.build_problem(int(args.day), args.debug)
        problem.part_one()
        problem.part_two()

    
    

if __name__ == '__main__':
    main()