import random


def solve():
    answer = random.randrange(10)
    while True:
        val = int(input("Input: "))
        if answer == val:
            print('정답')
            break
        elif answer > val:
            print('크다')
        else:
            print('작다')


if __name__ == '__main__':
    solve()
