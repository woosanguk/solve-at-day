"""
    https://www.hackerrank.com/challenges/kangaroo/problem
"""


def solve(x1, v1, x2, v2):
    if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    print(solve(0, 3, 4, 2))
    print(solve(0, 2, 5, 3))
