def solve(a, b):
    pivot = a
    if pivot < b:
        pivot = b
    max = 0
    for i in range(1, pivot + 1):
        if a % i == 0 and b % i == 0:
            max = i
        if i == a or i == b:
            break
    return max


if __name__ == '__main__':
    print(solve(280, 30))
