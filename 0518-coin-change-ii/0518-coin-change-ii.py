class Solution(object):
    def change(self, amount, coins):
        n=len(coins)  # dp[i][j] number of ways to get j money using first i coins
        dp=[[0 for _ in range(amount + 1)] for _ in range(n+1)] 
        for i in range(n+1):
            dp[i][0] = 1
        
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if coins[i-1] <= j:
                    # Możemy wziąć monetę lub nie
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    # Nie możemy wziąć tej monety
                    dp[i][j] = dp[i-1][j]
        return dp[n][amount]
