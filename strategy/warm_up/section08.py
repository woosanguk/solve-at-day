def solve(a, b):
    if b != 0:
        return solve(b, a % b)
    else:
        return a


if __name__ == '__main__':
    print(solve(280, 30))
