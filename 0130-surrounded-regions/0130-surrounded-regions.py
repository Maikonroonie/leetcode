class Solution(object):
    def solve(self, board):
        stack=[]
        n=len(board)
        m=len(board[0])
        for i in range(m):
            if board[0][i]=='O':
                stack.append((0, i))
            if board[n-1][i]=='O':
                stack.append((n-1, i))
        for i in range(n):
            if board[i][0]=='O':
                stack.append((i, 0))
            if board[i][m-1]=='O':
                stack.append((i, m-1))
        visited=set()
        while stack:
            x, y = stack.pop()
            visited.add((x, y))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m and board[nx][ny]=='O' and (nx, ny) not in visited:
                    stack.append((nx, ny))
                    visited.add((nx, ny))
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j]='X'
        

