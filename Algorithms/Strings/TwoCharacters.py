"""
    https://www.hackerrank.com/challenges/two-characters/problem
"""

import re


def check_character_from(str):
    temp = ""
    for s in str:
        if s == temp:
            return False
        temp = s
    return True


def two_characters_solve(n, string):
    data = {}

    for s in string:
        if s in data:
            data[s] += 1
        else:
            data[s] = 1
    data = sorted(data, key=data.get, reverse=True)
    ret = 0
    if len(data) > 2:
        for i in range(0, len(data)):
            for j in range(i + 1, len(data)):
                new_srt = re.sub('[^%c|%c]'%(data[i], data[j]), '', string)
                if check_character_from(new_srt):
                    if ret < len(new_srt):
                        ret = len(new_srt)
    elif len(data) == 2:
        if check_character_from(string):
            ret = len(string)
    return ret


if __name__ == "__main__":
    print("result = ", two_characters_solve(10, "beabeefeab"))
    print("result = ", two_characters_solve(0, "a"))
    print("result = ", two_characters_solve(0, "aa"))
    print("result = ", two_characters_solve(0, "ab"))
    print("result = ", two_characters_solve(0, "acbafbacbaeb"))