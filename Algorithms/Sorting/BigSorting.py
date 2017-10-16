"""
    https://www.hackerrank.com/challenges/big-sorting/problem
"""


def solve(n, x):
    result = sorted(x, key=lambda x: int(x))
    return result


if __name__ == "__main__":
    print("result = ", solve(6, ['31415926535897932384626433832795', '1', '3', '10', '3', '5']))
