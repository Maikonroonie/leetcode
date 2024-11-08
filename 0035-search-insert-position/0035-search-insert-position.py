class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)
        left, right= 0, l-1
        while left<=right:
            mid=(left + right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else: right=mid-1
        return left

                


        