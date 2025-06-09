class Solution(object):
    def lengthOfLIS(self, nums):
        n=len(nums) # bottom up O(n^2)
        if n==0:
            return 0

        dp=[1 for _ in range(n+1)] # longest len of lis that ends on the idx i

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# top - bottom
'''class Solution(object): 
    def lengthOfLIS(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        memo = [-1] * n  # -1 oznacza "jeszcze nie obliczono"

        def dp(i):
            if memo[i] != -1:
                return memo[i]

            max_len = 1  # sam nums[i]
            for j in range(i):
                if nums[j] < nums[i]:
                    max_len = max(max_len, dp(j) + 1)

            memo[i] = max_len
            return memo[i]

        result = 1
        for i in range(n):
            result = max(result, dp(i))

        return result'''
