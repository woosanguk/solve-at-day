"""
    https://www.hackerrank.com/challenges/icecream-parlor/problem
"""


def ice_cream_parlor_solve(m, n, flavor):
    for i in range(n):
        for j in range(i + 1, n):
            if flavor[i] + flavor[j] == m:
                print(i + 1, j + 1)
                return


if __name__ == "__main__":
    ice_cream_parlor_solve(4, 5, [1, 4, 5, 3, 2])
    ice_cream_parlor_solve(4, 4, [2, 2, 4, 3])