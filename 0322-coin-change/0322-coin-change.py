class Solution(object):
    def coinChange(self, coins, amount):
        dp=[float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i-coin >=0:
                    dp[i] = min(dp[i-coin] + 1, dp[i])
        return dp[amount] if dp[amount] != float('inf') else -1
