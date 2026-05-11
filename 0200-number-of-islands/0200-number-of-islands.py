class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        q = deque()
        visited = set()
        n = len(grid)
        m = len(grid[0])

        def bfs(i, j):
            q = deque()
            visited.add((i, j))
            q.append((i, j))

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '1' and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
                            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i, j) not in visited:
                    res += 1
                    bfs(i, j)

        return res
                    
        