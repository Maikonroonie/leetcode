
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # heap of tuples (time_so_far, i, j)
        heap = [(grid[0][0], 0, 0)]
        visited = [[False for _ in range(n)] for _ in range(n)]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while heap:
            t, i, j = heapq.heappop(heap)
            if visited[i][j]:
                continue
            visited[i][j] = True
            if i == n-1 and j == n-1:
                return t
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                    nt = max(t, grid[ni][nj])
                    heapq.heappush(heap, (nt, ni, nj))

