class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def f(i, j):
            return ((nums[i]-1)*(nums[j]-1))

        nums.sort(reverse = True)
        return f(0, 1)
        # co to jest za zadanie xdddd


        