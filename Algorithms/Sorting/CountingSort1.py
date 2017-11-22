"""
    https://www.hackerrank.com/challenges/countingsort1/problem
"""


def counting_sort_1_solve(n, arr):
    data = {}
    for a in arr:
        if int(a) in data:
            data[int(a)] += 1
        else:
            data[int(a)] = 1

    for i in range(100):
        if i in data:
            print(data[i], end=' ')
        else:
            print("0", end=' ')


if __name__ == "__main__":
    counting_sort_1_solve(5, [2, 4, 6, 8, 3])