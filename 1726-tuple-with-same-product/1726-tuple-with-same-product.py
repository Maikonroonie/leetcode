class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                x = nums[i] * nums[j]
                if x in d:
                    res += 8*(d[x])
                else:
                    d[x] = 0
                d[x] += 1
        return res
