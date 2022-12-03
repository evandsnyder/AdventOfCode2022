from problems import *


class ProblemFactory:
    def __init__(self):
        pass

    def build_problem(self, day: int, debug: bool) -> Problem:
        # Need to generat filename and class itself..
        filename = "input/"
        if debug:
            filename += "sample.txt"
        else:
            filename += f"input_day_{day}.txt"

        match day:
            case 1:
                print("Building day one...")
                return DayOne(filename, debug)
            case 2:
                return DayTwo(filename, debug)
            case 3:
                return DayThree(filename, debug)
            case 4:
                return DayFour(filename, debug)
            case 5:
                return DayFive(filename, debug)
            case 6:
                return DaySix(filename, debug)
            case 7:
                return DaySeven(filename, debug)
            case 8:
                return DayEight(filename, debug)
            case 9:
                return DayNine(filename, debug)
            case 10:
                return DayTen(filename, debug)
            case 11:
                return DayEleven(filename, debug)
            case 12:
                return DayTwelve(filename, debug)
            case 13:
                return DayThirteen(filename, debug)
            case 14:
                return DayFourteen(filename, debug)
            case 15:
                return DayFifteen(filename, debug)
            case 16:
                return DaySixteen(filename, debug)
            case 17:
                return DaySeventeen(filename, debug)
            case 18:
                return DayEighteen(filename, debug)
            case 19:
                return DayNineteen(filename, debug)
            case 20:
                return DayOne(filename, debug)
            case 21:
                return DayTwentyOne(filename, debug)
            case 22:
                return DayTwentyTwo(filename, debug)
            case 23:
                return DayTwentyThree(filename, debug)
            case 24:
                return DayTwentyFour(filename, debug)
            case 25:
                return DayTwentyFive(filename, debug)
            case _:
                raise NotImplementedError()
