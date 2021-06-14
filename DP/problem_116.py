"""
Counting Block Combinations
"""


def counting_blocks(m, n):

    dp = [1] * (n) + [0] * (m - n + 1)  ## [1, 1, 0, 0, 0, 0]

    for i in range(n, m + 1):  # [2, 3, 4, 5]

        dp[i] += dp[i - 1] + dp[i - n]  # dp[2] = dp[1]+dp[0] = 2
        # dp[3] = dp[2] + dp[1] = 3
        # dp[4] = dp[3]+ dp[2] = 5
        # dp[5] = dp[4] + dp[3] = 8
    return dp[m] - 1


def fib_(m, n):
    dp = [1] * n + [0] * (m - n + 1)

    for i in range(n, m + 1):
        if i < 2:
            dp[i] = 1
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
    return dp[m] - 1


if __name__ == "__main__":
    # m, n = map(int, input().split())
    # m, n = 7, 3
    print(counting_blocks(50, 2) + counting_blocks(50, 3) + counting_blocks(50, 4))
    print(counting_blocks(5, 1))
    print(fib_(50, 2) + fib_(50, 3) + fib_(50, 4))
