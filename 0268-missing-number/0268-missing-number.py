class Solution(object):
    def missingNumber(self, nums):
    #    nums.sort()
     #   for i in range(len(nums)-1):
      #      if nums[i]+1==nums[i+1]:
       #         continue
        #    else:
         #       return nums[i]+1
        #return nums[-1]+1 if nums[0]==0 else 0

    #now lest solve it with O(n) time and O(1) space by using sum of aritmetic sequence
        suma=0
        n=len(nums)
        for i in range(n):
            suma+=nums[i]
        return ((n)*(n+1)//2 - suma)