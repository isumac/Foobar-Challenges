
def solution(n):
    # this is a problem pertaining to Euler's partitioning of integers
    # using formula for Distinct Partitions of the form (1 + x)(1 + x^2)(1 + x^3)...(1 + x^n) = Dp for n
    dp = [[0] * n for _ in range(n + 1)] 
    
    dp[0][0] = 1 # initialise for 1
    for j in range(1, n):
        for i in range(n + 1):
            dp[i][j] = dp[i][j - 1]
            if i >= j:
                dp[i][j] += dp[i - j][j - 1]

    return dp[-1][-1]




