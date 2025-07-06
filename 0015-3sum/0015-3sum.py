class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            num = nums[i]
            target = -num
            left = i + 1
            right = n - 1

            while left < right:
                s = nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    res.append((num, nums[left], nums[right]))
                    prev_left = nums[left]
                    prev_right = nums[right]
                    left += 1
                    right -= 1
                    while left < right and nums[left] == prev_left:
                        left += 1
                    while left < right and nums[right] == prev_right:
                        right -= 1

        return res
