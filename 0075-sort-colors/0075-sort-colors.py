class Solution(object):
    def sortColors(self, nums):
        T=[0,0,0]
        n=len(nums)
        for i in range(n):
            T[nums[i]]+=1
            x=0
            y=0
            z=0
        for i in range(n):
            if x<T[0]:
                nums[i]=0
                x+=1
            elif y<T[1]:
                nums[i]=1
                y+=1
            else:
                nums[i]=2
        return nums