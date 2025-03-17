class Solution(object):
    def twoSum(self, nums, target):
        mapa={}  #1 O(n) time    O(n) space
        n=len(nums)
        for i in range(n):
            val=target-nums[i]
            if val in mapa:
                return mapa[val], i
            mapa[nums[i]] = i
    #def twoSum(self, nums, target):
     #   nums.sort()# mozna posorotwac samemu heap sortem/ merge sortem/quick sortem/ w nlogn time
      #  l=0
       # r=len(nums)-1
        #while l<r:
         #   if nums[l]+nums[r]==target:
          #      return l, r
           # elif nums[l]+nums[r]<target:  # jeszcze zeby to mialo sens trzeba by zrobic tablice krotek dla zachowania indeksow
            #        l+=1
             #   else nums[l]+nums[r]>target:
              #      r-=1
            #return 
            

        
        
