class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        suma = sum(nums)
        return suma % k       