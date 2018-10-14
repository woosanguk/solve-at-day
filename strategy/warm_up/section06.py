def solve(n):
    result = []
    for val in range(1, n + 1):
        is_prime = True
        for i in range(2, val):
            if val % i == 0:
                is_prime = False
                break
        if is_prime:
            result.append(val)
    print(result)


if __name__ == '__main__':
    solve(1000)
