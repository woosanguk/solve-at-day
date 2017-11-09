"""
    https://www.hackerrank.com/challenges/camelcase/problem
"""


def camel_case_solve(string):
    result = 1
    for s in string:
        if s.isupper():
            result += 1
    return result


if __name__ == "__main__":
    print("result = ", camel_case_solve('saveChangesInTheEditor'))
