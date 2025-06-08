class Solution(object):
# wystarczy uruchomic klasyczy rob house tyle ze dla dwoch przypadkow 1) bez rabowania pierwszego domu, 
# 2 bez rabowania ostatniego domu

    def rob(self, nums):
        n=len(nums)
        def rob_1(nums):
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
        if n==1:
            return nums[0]
        return max(rob_1(nums[1:]), rob_1(nums[:n-1]))
