'''class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(nums) - 1:
                return True
            if nums[i] == 0:
                return False

            end = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, end):
                if dfs(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False

        return dfs(0)'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        for i, jump in enumerate(nums):
            if i > far:           # nie doskoczyliśmy do i
                return False
            far = max(far, i + jump)
        return True
