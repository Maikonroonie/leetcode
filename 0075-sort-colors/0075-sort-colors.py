class Solution(object):
    def sortColors(self, nums):
        '''T=[0,0,0]
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
        return nums'''
        #partition
        def swap(a,b):
            nums[a], nums[b] = nums[b], nums[a]
        l=0
        r=len(nums)-1
        i=0
        while i<=r:
            if nums[i]==0:
                swap(i, l)
                l+=1
            elif nums[i]==2:
                swap(i, r)
                i-=1
                r-=1
            i+=1
        return nums
                
