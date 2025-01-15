class Solution(object):
    def maximalSquare(self, matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        maximum=0

        for row in range(rows-1,-1,-1):
            for col in range(cols-1,-1,-1):
                if matrix[row][col]!="0":
                    if row+1<rows and col+1<cols:
                        dp[row][col]=min(dp[row+1][col+1],dp[row+1][col],dp[row][col+1])+1
                    else:
                        dp[row][col]=1
                    maximum=max(maximum, dp[row][col])
        return maximum*maximum
