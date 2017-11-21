"""
    https://www.hackerrank.com/challenges/insertionsort1/problem
"""


def print_arr(arr):
    for a in arr:
        print(a, end=' ')
    print()


def insertion_sort_part_2_solve(n, arr):
    for i in range(n):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
            print_arr(arr)
        arr[j] = temp
    print_arr(arr)


if __name__ == "__main__":
    insertion_sort_part_2_solve(5, [2, 4, 6, 8, 3])