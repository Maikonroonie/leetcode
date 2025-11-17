class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cols = [0 for _ in range(m)]
        rows = [0 for _ in range(n)]
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    rows[row] += 1
                    cols[col] += 1
        res = 0
        for row, o1 in enumerate(rows):
            for col, o2 in enumerate(cols):
                if grid[row][col] == 1:
                    res += (o1 - 1)*(o2 - 1)
        return res

