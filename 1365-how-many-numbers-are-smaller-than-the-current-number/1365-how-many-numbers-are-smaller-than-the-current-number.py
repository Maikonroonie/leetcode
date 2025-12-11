class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [ 0 for _ in range(n)]
        d = {}
        sorted_nums = sorted(nums)
        for i, num in enumerate(sorted_nums):
            if num not in d:
                d[num] = i
        
        for i, num in enumerate(nums):
            res[i] = d[num]
        return res