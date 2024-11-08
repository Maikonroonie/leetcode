class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=len(nums)
        x=0
        for i in range(l):
            if nums[i]==val:
                x+=1
        k=l-x
        nums[:]=[nums[i] for i in range(l) if nums[i]!=val]
        return k


        