class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefixsum and n^2 is easy
        # can it be done faster?
        n = len(nums)
        res = 0
        cur_sum = 0
        d = {0:1}
        for num in nums:
            cur_sum += num
            target = cur_sum - k
            if target in d:
                res += d[target]
            
            if cur_sum in d:
                d[cur_sum] += 1
            else:
                d[cur_sum] = 1
        return res