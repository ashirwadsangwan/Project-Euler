"""
Counting Block Combinations
"""
def counting_blocks(m, n):

    dp = [1]*(n) + [0]*(m-n+1)

    for i in range(n, m+1):
        if i < 3:
            dp[i] = 1
        else:
            dp[i] = dp[i-1] + sum(dp[:i-n]) + 1
    return dp[m]


if __name__ == "__main__":
    m, n = map(int, input().split())
    # m, n = 7, 3
    print(counting_blocks(m, n))
