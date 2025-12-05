class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0 for _ in range(n)]
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
        sufix = [0 for _ in range(n)]
        sufix[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            sufix[i] = sufix[i+1] + nums[i]
        
        res = 0

        for i in range(n-1):
            if (prefix[i] - sufix[i+1]) % 2 == 0:
                res += 1
        return res