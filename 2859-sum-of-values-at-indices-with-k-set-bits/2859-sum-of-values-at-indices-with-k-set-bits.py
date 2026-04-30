class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        if k == 0: return nums[0]
        d, j, res = [0] * len(nums), 1, 0
        for i in range(1, len(nums)):
            if j * 2 == i: j *= 2
            d[i] = 1 + d[i - j]
            if d[i] == k: res += nums[i]

        return res
