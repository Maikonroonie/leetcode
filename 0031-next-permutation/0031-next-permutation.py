class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        break_outer2=False
        break_outer=False
        x=len(nums)-1
        y=len(nums)-2
        for i in range(len(nums)-1,-1,-1):
            for j in range(i-1,-1,-1):
                for k in range(i,j,-1):
                    if nums[k]>nums[j]:
                        nums[k], nums[j] =nums[j], nums[k]
                        break_outer=True
                        break_outer2=True
                        break
                if break_outer2:
                    break
                y-=1
            if break_outer:
                break
            x-=1
            y=x-1
        if x==-1:
            nums.reverse()
        else:
            part1=nums[:y+1]
            part2=nums[y+1:]
            part2.sort()
            nums[:]=part1 + part2
            
            