class Solution(object):
    def maxAreaOfIsland(self, grid):
        max_curr=0
        n=len(grid)
        m=len(grid[0])
        visited=set()
        def rek(i,j):
            if i<0 or i>=n or j<0 or j>=m:
                return 0
            if grid[i][j]!=1 or (i, j) in visited:
                return 0
            visited.add((i ,j))
            return (1+ rek(i+1, j) + rek(i-1, j) + rek(i, j+1) + rek(i, j-1))

        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j]==1:
                    max_curr=max(rek(i, j), max_curr)
        return max_curr

