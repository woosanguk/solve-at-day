"""
    https://www.hackerrank.com/challenges/countingsort2/problem
"""


def counting_sort_2_solve(n, arr):
    ret = sorted(arr)
    for v in ret:
        print(v, end=" ")


if __name__ == "__main__":
    counting_sort_2_solve(6, [2, 4, 6, 8, 3, 3])