"""
    https://www.hackerrank.com/challenges/migratory-birds/problem
"""


def migratory_birds_solve(n, ar):

    type = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0
    }
    for bird in ar:
        type[bird] += 1
    most = -1
    ret = 0
    for key, val in type.items():
        if most < val:
            most = val
            ret = key
    return ret


if __name__ == "__main__":
    print(migratory_birds_solve(6, [1, 4, 4, 4, 5, 3]))


