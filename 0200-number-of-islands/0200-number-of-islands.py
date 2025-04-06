class Solution(object):
    def numIslands(self, grid):
        visited=set()
        n=len(grid)
        m=len(grid[0])
        cntr=0
        def search(i, j):
            if i<0 or i>=n or j<0 or j>=m:
                return
            if grid[i][j]!='1' or (i, j) in visited:
                return
            visited.add((i, j))
            search(i+1, j)
            search(i-1, j)
            search(i, j+1)
            search(i, j-1)

        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j]=='1':
                    cntr+=1
                    search(i, j)


        return cntr