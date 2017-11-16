"""
    https://www.hackerrank.com/challenges/big-sorting/problem
"""


def correctness_and_the_loop_invariant_solve(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while (j > -1) and (l[j] > key):
            l[j + 1] = l[j]
            j -= 1
        l[j+1] = key
    return l


if __name__ == "__main__":
    print("result = ", correctness_and_the_loop_invariant_solve([4, 1, 3, 5, 6, 2]))
