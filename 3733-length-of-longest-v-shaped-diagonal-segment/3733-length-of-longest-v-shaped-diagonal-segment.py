class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:        
        @lru_cache(None)
        def dfs(row,col, dr,dc, element, hasTurned):
            if not (0 <= row < m and 0 <= col < n) or grid[row][col] != element:
                return 0            
            ans = dfs(row + dr, col + dc, dr, dc, element^2, hasTurned)
            if hasTurned: return ans + 1
            length = dfs(row + dc, col - dr, dc, -dr, element^2, True)
            return max(ans,length) + 1 
        m, n = len(grid), len(grid[0])
        ans, dr, dc, hasOne = 0, 1, 1, False 
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    hasOne = True
                    for _ in range(4):
                        dr, dc = -dc, dr
                        vee = dfs(row + dr, col + dc, dr, dc, 2, False)
                        ans = max(ans, vee)
        return ans + hasOne







'''
class Solution:
    DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    def lenOfVDiagonal(self, grid):
        m, n = len(grid), len(grid[0])
        memo = [[[0] * (1 << 3) for _ in range(n)] for _ in range(m)]
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                maxs = [m - i, j + 1, i + 1, n - j]
                for k in range(4):
                    if maxs[k] > ans:
                        ans = max(ans, self.dfs(i, j, k, 1, 2, grid, memo) + 1)
        return ans

    def dfs(self, i, j, k, canTurn, target, grid, memo):
        m, n = len(grid), len(grid[0])
        i += self.DIRS[k][0]
        j += self.DIRS[k][1]
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != target:
            return 0

        mask = (k << 1) | canTurn
        if memo[i][j][mask] > 0:
            return memo[i][j][mask]

        res = self.dfs(i, j, k, canTurn, 2 - target, grid, memo)
        if canTurn == 1:
            maxs = [m - i - 1, j, i, n - j - 1]
            nk = (k + 1) % 4
            if maxs[nk] > res:
                res = max(res, self.dfs(i, j, nk, 0, 2 - target, grid, memo))
        memo[i][j][mask] = res + 1
        return memo[i][j][mask]
        '''