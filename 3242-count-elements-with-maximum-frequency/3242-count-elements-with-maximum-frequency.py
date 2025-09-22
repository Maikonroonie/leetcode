class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        n=len(nums)
        d = {}
        for num in nums:
            if num not in d:
                d[num]  = 1 
            else:
                d[num] += 1
        maxVal = -inf
        res = 0
        print(d)
        for k, v in d.items():
            if v > maxVal:
                res = v
                maxVal = v
            elif v  == maxVal:
                res += v
        return res