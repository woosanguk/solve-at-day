"""
    https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem
"""


def solve(n, k, x):
    x.sort()
    index = 0
    transmitter = 0
    while index < n:
        transmitter += 1
        inner_index = index
        current = x[index]
        installed = False
        while inner_index < n:
            if inner_index + 1 >= n:
                index = inner_index + 1
                break
            if not installed:
                if current + k >= x[inner_index + 1]:
                    inner_index += 1
                else:
                    current = x[inner_index]
                    installed = True
            else:
                if current + k >= x[inner_index + 1]:
                    inner_index += 1
                    continue
                else:
                    index = inner_index + 1
                    break

    return transmitter


if __name__ == "__main__":
    print("Hacker Land Radio Transmitters")
    print("result =", solve(5, 1, [1, 2, 3, 4, 5]))
    print("result =", solve(8, 2, [7, 2, 4, 6, 5, 9, 12, 11]))
