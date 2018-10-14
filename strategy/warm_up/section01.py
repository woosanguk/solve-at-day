def solve(val, type):
    if str(type).upper() == 'A':
        return hex(val)
    elif str(type).upper() == 'B':
        return int(val)
    return None


if __name__ == '__main__':
    print(solve(10, 'a'))
    print(solve(0xa, 'b'))
