class Solution(object):
    def generateParenthesis(self, n):
        res=[]
        stack = []
        def backtrack(open_cnt, close_cnt):
            if open_cnt == close_cnt == n:
                res.append("".join(stack))
    #1 adding (      
            if open_cnt<n:
                stack.append('(')
                backtrack(open_cnt+1, close_cnt)
                stack.pop() #backtrack
    #2 adding )
            if close_cnt<open_cnt:
                stack.append(')')
                backtrack(open_cnt, close_cnt+1)
                stack.pop() # backtrack

        backtrack(0, 0)
        return res