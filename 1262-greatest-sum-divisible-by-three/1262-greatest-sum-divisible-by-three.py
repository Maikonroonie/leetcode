class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        #dp[i] - maksymalna suma z reszta i (0, 1, 2)
        for num in nums:
            for max_sum in dp[:]: #kopia zeby nie zmieniac tablicy podczas dzialania
                a = max_sum + num
                dp[a % 3] = max(dp[a % 3], a)

        return dp[0]

        
        
