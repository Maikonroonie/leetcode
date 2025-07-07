class Solution(object):
    def trap(self, height):
        # prefix and sufix sollution
        # left - prefix, right - sufix etc 
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

# basiclly the same solution but with two pointers and so on space is O(n) so yeah two pointers
# little bit better
        ''' 
        class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
        '''
