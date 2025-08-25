class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        res = [None for _ in range(n*m)]
        diagonals = {}

        for i in range(n):
            for j in range(m):
                if i + j not in diagonals:
                    diagonals[i + j] = []
                diagonals[i + j].append(mat[i][j])
        res = []
        for k in range(n + m - 1):
            if k % 2 == 0:
                res.extend(diagonals[k][::-1])  # odwracamy
            else:
                res.extend(diagonals[k])        # normalnie
        return res
