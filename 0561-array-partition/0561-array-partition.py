class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(0, n, 2):
            n1 = nums[i]
            n2 = nums[i+1]
            res += min(n1, n2)
        return res