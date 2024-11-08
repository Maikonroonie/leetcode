class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x=0
        l=len(nums)
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[l-1]+1
                x+=1
        nums.sort()
        k=l-x
        return k

        