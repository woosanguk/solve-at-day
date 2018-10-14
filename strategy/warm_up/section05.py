def solve(n):
    result = []
    for i in range(1, 1001):
        if i % n == 0:
            result.append(i)

    return len(result), sum(result)


if __name__ == '__main__':
    print(solve(4))
