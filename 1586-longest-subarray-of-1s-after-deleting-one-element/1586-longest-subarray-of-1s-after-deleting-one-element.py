class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        #sliding window
        l = 0
        max_res = 0
        cur_res = 0
        cnt=0

        for r in range(n):
            if nums[r] == 0:
                cnt+=1
            
            while cnt>1:
                if nums[l] == 0:
                    cnt-=1
                l+=1
            
            max_res = max(max_res, r - l) # it is basiclly r-l + 1 - 1
        
        return max_res


'''
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]  # dp[i][0] bez usunięcia, dp[i][1] z jednym usunięciem

        if nums[0] == 1:
            dp[0][0] = 1
        
        ans = 0
        for i in range(1, n):
            if nums[i] == 1:
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = dp[i-1][1] + 1
            else:  # nums[i] == 0
                dp[i][0] = 0
                dp[i][1] = dp[i-1][0]  # usuwamy to zero

            ans = max(ans, dp[i][0], dp[i][1])
        
        # jeśli wszystkie były jedynkami, musimy usunąć jedną
        if all(x == 1 for x in nums):
            return n - 1
        return ans
'''