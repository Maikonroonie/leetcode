class Solution(object):
    def twoSum(self, nums, target):
        mapa={}
        n=len(nums)
        for i in range(n):
            val=target-nums[i]
            if val in mapa:
                return mapa[val], i
            mapa[nums[i]] = i
        
        
