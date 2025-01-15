class Solution(object):
    def containsDuplicate(self, nums):
        N=len(nums)
        nums.sort()
        if N==1:
            return False
        for i in range(N-1):
            if nums[i]==nums[i+1]:
                return True
        return False
