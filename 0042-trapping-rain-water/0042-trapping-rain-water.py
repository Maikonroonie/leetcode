class Solution(object):
    def trap(self, height):
        n=len(height)
        left=[0 for _ in range(n)]
        right = [0 for _ in range(n)]
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])

        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        
        normalize=[ 0 for _ in range(n)]
        for i in range(n):
            normalize[i] = min(left[i], right[i])
        
        res=0
        for i in range(n):
            res+=normalize[i] - height[i]
        
        return res
