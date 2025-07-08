class Solution(object):
    def largestRectangleArea(self, heights):
        n=len(heights)
        next_smaller=[-1 for _ in range(n)]
        prev_smaller=[-1 for _ in range(n)]
        stack1=[]
        stack2=[]
        # next smaller
        for i in range(n-1, -1, -1):
            while stack1 and heights[stack1[-1]] >= heights[i]:
                stack1.pop()
            if stack1:
                next_smaller[i] = stack1[-1]
            stack1.append(i)
        
        #prev smaller
        for i in range(n):
            while stack2 and heights[stack2[-1]] >= heights[i]:
                stack2.pop()
            if stack2:
                prev_smaller[i] = stack2[-1]
            stack2.append(i)
        
        # teraz area dla i = heihgts[i] * (next_smaller - prev_smaller)
        max_area = 0
        cur_area = 0
        for i in range(n):
            if next_smaller[i] != -1 and prev_smaller[i] != -1:
                cur_area = heights[i] * (next_smaller[i] - prev_smaller[i] -1)
                max_area = max(cur_area, max_area)
            if prev_smaller[i] == -1 and next_smaller[i]!= -1:
                cur_area = heights[i] * ( next_smaller[i] )
                max_area = max(cur_area, max_area)
            if prev_smaller[i] != -1 and next_smaller[i] == -1:
                cur_area = heights[i] * ( n - prev_smaller[i]-1)
                max_area = max(cur_area, max_area)
            if prev_smaller[i] == -1 and next_smaller[i] == -1:
                cur_area = heights[i] * (n)
                max_area = max(cur_area, max_area)
           # print((cur_area, next_smaller[i], prev_smaller[i]))        
        return max_area
        