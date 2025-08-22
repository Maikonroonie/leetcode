class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        A = deque()
        max_left = float('inf')
        max_right = float('-inf')
        max_up = float('inf')
        max_down = float('-inf')

        for y in range(n):
            for x in range(m):
                if grid[y][x] == 1:
                    max_left = min(x, max_left)
                    max_right = max(x, max_right)
                    max_up = min(y, max_up)
                    max_down = max(y, max_down)
        
        area = (max_right - max_left + 1) * (max_down - max_up + 1)
        return area