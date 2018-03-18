"""
정수 배열(int array)가 주어지면 가장 큰 이어지는 원소들의 합을 구하시오. 단, 시간복잡도는 O(n).

예제}

Input: [-1, 3, -1, 5]

Output: 7 // 3 + (-1) + 5

Input: [-5, -3, -1]

Output: -1 // -1

Input: [2, 4, -2, -3, 8]

Output: 9 // 2 + 4 + (-2) + (-3) + 8
"""


def do(input):
    max_sum = input[0]
    current_sum = input[0]
    for i in range(1, len(input)):
        current_sum = max(current_sum + input[i], input[i])
        max_sum = max(current_sum, max_sum)
    return max_sum


def do_1(input):
    max = input[0]

    for i in range(0, len(input)):
        cal_sum = input[i]
        for j in range(i + 1, len(input)):
            cal_sum += input[j]
            # cal_sum = get_sum(input, i, j)
        if cal_sum > max:
            max = cal_sum
    return max


def get_sum(values, start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += values[i]
    return sum
