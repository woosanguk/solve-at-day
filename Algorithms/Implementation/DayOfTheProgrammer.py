"""
    https://www.hackerrank.com/challenges/day-of-the-programmer/problem
"""


def day_of_the_programmer_solve(year):
    base_day = 31 + 31 + 30 + 31 + 30 + 31 + 31
    if year <= 1917:
        if year % 4 == 0:
            base_day += 29
        else:
            base_day += 28
    elif year == 1918:
        base_day += 15
    else:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            base_day += 29
        else:
            base_day += 28
    return "%d.09.%d" % (256 - base_day, year)


if __name__ == "__main__":
    print(day_of_the_programmer_solve(2017))
    print(day_of_the_programmer_solve(2016))
    print(day_of_the_programmer_solve(1918))


