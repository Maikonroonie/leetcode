class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix_sum = [0 for _ in range(n)]
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        return prefix_sum
        