class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        nums.sort()
        n = len(nums)
        l = 0 
        r = n - 1
        res = 0
        while l <= r:
            if nums[r] + nums[l] <= limit:
                res += 1
                l += 1
                r -= 1
            elif nums[r] <= limit:
                res += 1
                r -= 1

        return res

