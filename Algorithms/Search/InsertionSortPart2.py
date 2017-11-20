
def print_arr(arr):
    for a in arr:
        print(a, end=' ')
    print()


def solve(n, arr):
    for i in range(n):
        temp = arr[i]
        j = i

        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp
        if i > 0:
            print_arr(arr)


if __name__ == "__main__":
    solve(6, [1, 4, 3, 5, 6, 2])