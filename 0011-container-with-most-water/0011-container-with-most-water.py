class Solution:
    def maxArea(self, height: List[int]) -> int:
        temp_area=0
        max_area=0
        left=0
        right=len(height)-1
        while left<right:
            temp_area=(right-left)*min(height[left], height[right])
            max_area=max(temp_area, max_area)
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return max_area
