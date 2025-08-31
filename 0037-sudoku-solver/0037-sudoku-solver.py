from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 9
        rows = [[0] * (n+1) for _ in range(n)]
        cols = [[0] * (n+1) for _ in range(n)]
        boxes = [[0] * (n+1) for _ in range(n)]
        isSolved = False

        def canPlace(num, row, col):
            i = (row // 3) * 3 + col // 3
            return rows[row][num] == 0 and cols[col][num] == 0 and boxes[i][num] == 0

        def placeNum(num, row, col):
            i = (row // 3) * 3 + col // 3
            rows[row][num] += 1
            cols[col][num] += 1
            boxes[i][num] += 1
            board[row][col] = str(num)

        def removeNum(num, row, col):
            i = (row // 3) * 3 + col // 3
            rows[row][num] -= 1
            cols[col][num] -= 1
            boxes[i][num] -= 1
            board[row][col] = '.'

        def placeNextNums(row, col):
            nonlocal isSolved
            if row == n-1 and col == n-1:
                isSolved = True
            elif col == n-1:
                backtrack(row+1, 0)
            else:
                backtrack(row, col+1)

        def backtrack(row, col):
            nonlocal isSolved
            if isSolved:
                return
            if board[row][col] == '.':
                for num in range(1, 10):
                    if canPlace(num, row, col):
                        placeNum(num, row, col)
                        placeNextNums(row, col)
                        if not isSolved:
                            removeNum(num, row, col)
            else:
                placeNextNums(row, col)

        # inicjalizacja struktur
        for i in range(n):
            for j in range(n):
                if board[i][j] != '.':
                    placeNum(int(board[i][j]), i, j)

        backtrack(0, 0)
