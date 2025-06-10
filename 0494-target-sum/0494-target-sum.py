class Solution(object):
    def findTargetSumWays(self, nums, target):
        n=len(nums)
        dp=[defaultdict(int) for _ in range(n+1)]

        dp[0][0] = 1 # #(0lements. 0 sum) 1 way (1 way to sum zero with first 0 elements)

        for i in range(n):
            for cur_sum, count in dp[i].items():
                dp[i+1][cur_sum+nums[i]] += count
                dp[i+1][cur_sum-nums[i]] += count
        return dp[len(nums)][target]



        '''
        n=len(nums)
        suma=sum(nums)
        dp=[0 for _ in range(2*suma)]
        dp[0] = 1
        cur=0
        for num in nums:
            for j in range(suma+1, -1,):
                dp[j] += dp[j-num]
        return dp[target]'''
