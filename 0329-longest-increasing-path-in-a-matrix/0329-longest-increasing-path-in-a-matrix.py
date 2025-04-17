class Solution(object):
    def longestIncreasingPath(self, matrix):
        n=len(matrix)
        m=len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]

        def dfs(x, y):
            if dp[x][y]:
                return dp[x][y]
            max_length=1

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0<=x+dx<n and 0<=y+dy<m:
                    if matrix[x+dx][y+dy] > matrix[x][y]:
                        max_length=max(1+dfs(x+dx, y+dy), max_length)

            dp[x][y] = max_length          
            return max_length

        max_len=1
        cur_len=1
        for i in range(n):
            for j in range(m):
                cur_len=dfs(i, j)
                max_len=max(max_len, cur_len)
        return max_len


        