class Solution(object):
    def orangesRotting(self, grid):
        n=len(grid)
        m=len(grid[0])
        q=deque()
        time=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append([i, j, 0])
        while q:
            cur = q.popleft()
            x, y = cur[0], cur[1]
            time = cur[2]
            for dx, dy in [(1,0), (-1, 0), (0,1), (0,-1)]:
                nx, ny = x+dx, y+dy
                if 0<= nx < n and 0 <=ny <m:
                    if grid[nx][ny]==1:
                        grid[nx][ny]=2
                        q.append([nx, ny, time+1])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1
        return time


