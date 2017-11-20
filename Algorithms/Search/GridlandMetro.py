"""
    https://www.hackerrank.com/challenges/gridland-metro/problem
"""


def gridland_metro_solve(n, m, k, track):
    total = n * m
    data = {}
    for t in track:
        for i in (range(t[1] - 1, t[2])):
            key = str(t[0]) + "_" + str(i)
            data[key] = 1
    return total - len(data)


if __name__ == "__main__":
    print(gridland_metro_solve(4, 4, 3, [[2, 2, 3], [3, 1, 4], [4, 4, 4]]))