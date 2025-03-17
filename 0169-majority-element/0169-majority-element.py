class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        cnt=1
        val=nums[0]
        for i in range(1, n):
            if cnt==0:
                val=nums[i]
                cnt+=1
            elif cnt>0:
                if nums[i]!=val:
                    cnt-=1
                else:
                    cnt+=1
        return val