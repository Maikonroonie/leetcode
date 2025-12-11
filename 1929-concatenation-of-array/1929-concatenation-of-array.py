class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        A = [0 for _ in range(2*n)]
        for i in range(2*n):
            A[i] = nums[i%n]
        return A