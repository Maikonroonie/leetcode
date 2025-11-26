class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        # minimum suma
        res = nums[0]
        A = nums[1:]
        A.sort()
        return res + A[0] + A[1]


