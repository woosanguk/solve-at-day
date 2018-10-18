def solve(size, data):
    s = [0] + [50000 * 10000] * int(size)
    for i in range(len(data)):
        j = 0
        while j <= size - data[i][1]:
            if s[j] + data[i][0] < s[j + data[i][1]]:
                s[j + data[i][1]] = s[j] + data[i][0]
            j += 1
    print(s[size])


if __name__ == '__main__':
    memory_size = 10
    data = [[4, 3], [5, 4], [7, 5]]
    solve(memory_size, data)
