class Solution(object):
    def maxArea(self, height):
        global_max = 0
        cur_max = 0
        n=len(height)
        left = 0
        right = n-1
       # cur_max = (right - left) *min(height[left], height[right])
        #global_max=max(global_max, cur_max)
        while left<right:
            cur_max = (right - left) *min(height[left], height[right])
            global_max=max(global_max, cur_max)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return global_max

