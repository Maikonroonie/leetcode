class Solution(object):
    def moveZeroes(self, nums):
        N=len(nums)
        a=0
        x=N-1
        for i in range(N):
            if nums[a]==0:
                for j in range(a+1,x+1):
                    nums[j-1]=nums[j]
                nums[x]=0
                x-=1
            else:
                a+=1
        return nums
                

