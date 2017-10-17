"""
    https://www.hackerrank.com/challenges/tutorial-intro/problem

    v = int(input().strip())
    n = int(input().strip())
    arr = [int(x_temp) for x_temp in input().strip().split(' ')]

"""


def solve(v, n, arr):
    return arr.index(v)


if __name__ == "__main__":
    print(solve(4, 6, [1, 4, 5, 7, 9, 12]))
