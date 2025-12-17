class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        p = prices[0]
        dp = [[0, -p, p] for _ in range(k+1)]

        for day in range(1, n):
            curr_price = prices[day]
            for trans in range(k, 0, -1):
                prev_profit = dp[trans -1][0]

                dp[trans][0] = max(dp[trans][0], dp[trans][1] + curr_price, dp[trans][2] - curr_price)
                dp[trans][1] = max(dp[trans][1], prev_profit - curr_price)
                dp[trans][2] = max(dp[trans][2], prev_profit + curr_price)
        
        return dp[k][0]
        