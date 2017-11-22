"""
    https://www.hackerrank.com/challenges/runningtime/problem
"""


def running_time_of_algorithms_solve(n, arr):
    count = 0
    for i in range(n):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
            count += 1
        arr[j] = temp
    return count


if __name__ == "__main__":
    print(running_time_of_algorithms_solve(5, [2, 1, 3, 1, 2]))
