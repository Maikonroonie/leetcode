class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        painted = [[False for _ in range(n)] for _ in range(m)]
        d = {}
        for i in range(m):
            for j in range(n):
                d[mat[i][j]] = (i, j)
        rows = [0 for _ in range(m)]
        cols = [0 for _ in range(n)]

        for i, num in enumerate(arr):
            row, col = d[num]
            if painted[row][col] == False:

                rows[row] += 1
                cols[col] += 1 
                painted[row][col] = True

                if rows[row] == n or cols[col] == m:
                    return i



