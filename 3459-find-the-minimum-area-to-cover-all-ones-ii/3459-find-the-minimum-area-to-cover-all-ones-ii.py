class Solution:
    def minimumSum(self, A: List[List[int]]) -> int:
        res = inf
        for _ in range(4):
            n, m = len(A), len(A[0])

            for i in range(1, n):
                a1 = self.minimumArea(A[:i])
                for j in range(1, m):
                    part2 = [row[:j] for row in A[i:]]
                    part3 = [row[j:] for row in A[i:]]
                    a2 = self.minimumArea(part2)
                    a3 = self.minimumArea(part3)
                    res = min(res, a1 + a2 + a3)
                
                for k in range(i+1, n):
                    part2 = A[i:k]
                    part3 = A[k:]
                    a2 = self.minimumArea(part2)
                    a3 = self.minimumArea(part3)
                    res = min(res, a1 + a2 + a3)
            A = self.rotate(A)
        return res
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

    def rotate(self, A: List[List[int]]) -> List[List[int]]:
        n, m = len(A), len(A[0])
        return [[A[i][j] for i in range(n-1, -1, -1)] for j in range(m)]