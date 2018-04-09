"""
정수(int)가 주어지면, 팰린드롬(palindrome)인지 알아내시오. 팰린드롬이란, 앞에서부터 읽으나 뒤에서부터 읽으나 같은 단어를 말합니다. 단, 정수를 문자열로 바꾸면 안됩니다.

예제)

Input: 12345

Output: False

Input: -101

Output: False

Input: 11111

Output: True

Input: 12421

﻿Output: True
"""


def do(input):
    if input < 0:
        return False
    number = []
    temp_input = input
    while True:
        if -0.01 <= temp_input <= 0.01:
            break
        number.append(temp_input % 10)
        temp_input = int(temp_input / 10)

    temp_input = input
    while True:
        l_number = temp_input % 10
        f_number = number.pop()
        # print(l_number, f_number)
        temp_input = int(temp_input / 10)
        if l_number != f_number:
            return False
        if temp_input < 1:
            break
    return True

