class Solution(object):
    def lengthOfLIS(self, nums):
        n=len(nums)
        if n==0:
            return 0

        dp=[1 for _ in range(n+1)] # longest len of lis to the n-th index

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
