class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        n = len(grid)
        m = len(grid[0])
        t = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j, 0))
        # now we start bfs with the rotten cells
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            r, c, t = q.popleft()
            for dr, dc in directions:
                nr, nc  = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc, t+1))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return t
