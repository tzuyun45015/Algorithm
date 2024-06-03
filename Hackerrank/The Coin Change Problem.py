#dp
def getWays(n, c):
    # Write your code here
    dp = [[0]* (n+1) for i in range(len(c)+1)]
    for i in range(len(c), -1, -1):
        dp[i][0] = 1
    
    for i in range(len(c)-1, -1, -1):
        for j in range(1, n+1):
            if j >= c[i]:
                dp[i][j] += dp[i][j - c[i]]
            dp[i][j] += dp[i+1][j] 
    return dp[0][n]
