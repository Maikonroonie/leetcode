class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack = []
        max_area = 0
        
        for i in range(n+1):
            h = heights[i] if i < n else 0
            while stack and heights[stack[-1]] > h:
                hg = heights[stack.pop()] # tablica przechowuje indeksy
                wg = i if not stack else i - stack[-1] -1
                max_area = max(max_area, hg*wg)
            stack.append(i)
        return max_area