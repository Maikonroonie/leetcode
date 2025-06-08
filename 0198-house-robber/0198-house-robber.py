class Solution(object):
    # dp[i] is the maximum money we can steal up to the i-th house with this house
    def rob(self, nums):
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        dp=[0 for i in range(n+1)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]
        