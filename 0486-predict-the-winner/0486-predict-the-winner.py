class Solution(object):
    def predictTheWinner(self, nums):

        def dfs(nums, p1, p2, i):
            if not nums:
                if p1>=p2:
                    return True
                else:
                    return False
            if i%2==0:
                return (dfs(nums[:-1], p1+nums[-1], p2, i+1) or dfs(nums[1:], p1+nums[0], p2, i+1))

            else:
                return (dfs(nums[:-1], p1, p2+nums[-1], i+1) and dfs(nums[1:], p1, p2+nums[0], i+1))
        return dfs(nums, 0, 0, 0)

        