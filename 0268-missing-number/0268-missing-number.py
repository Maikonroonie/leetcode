class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                continue
            else:
                return nums[i]+1
        return nums[-1]+1 if nums[0]==0 else 0