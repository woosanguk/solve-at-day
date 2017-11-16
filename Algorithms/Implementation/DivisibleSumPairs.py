"""
    https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
"""


def divisible_sum_pairs_solve(n, k, arr):
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j]) % k == 0:
                count += 1
    return count


if __name__ == '__main__':
    print(divisible_sum_pairs_solve(6, 3, [1, 3, 2, 6, 1, 2]))