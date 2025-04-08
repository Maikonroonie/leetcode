class Solution(object):
    def pacificAtlantic(self, heights):
        n=len(heights)
        m=len(heights[0])
        stack=[]
        set_P=set()
        visited=set()
        for i in range(n):
            stack.append((i, 0))
            set_P.add((i, 0))
            visited.add((i, 0))
        for j in range(m):
            stack.append((0, j))
            set_P.add((0, j))
            visited.add((0, j))


        while stack:
            x, y = stack.pop()
            visited.add((x, y))
            for dx, dy, in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <=nx<n and 0<=ny<m and (nx, ny) not in visited:
                    if heights[nx][ny]>=heights[x][y]:
                        visited.add((nx, ny))
                        stack.append((nx, ny))
                        set_P.add((nx, ny))
        visited2=set()
        stack2=[]
        set_A=set()
        for i in range(n):
            stack2.append((i, m-1))
            set_A.add((i, m-1))
            visited2.add((i, m-1))
        for j in range(m):
            stack2.append((n-1, j))
            set_A.add((n-1, j))
            visited2.add((n-1, j))


        while stack2:
            x, y = stack2.pop()
            visited2.add((x, y))
            for dx, dy, in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <=nx<n and 0<=ny<m and (nx, ny) not in visited2:
                    if heights[nx][ny]>=heights[x][y]:
                        visited2.add((nx, ny))
                        stack2.append((nx, ny))
                        set_A.add((nx, ny))
        result=[]
        for i in range(n):
            for j in range(m):
                if (i, j) in set_A and (i, j) in set_P:
                    result.append((i, j))
        print(set_A)
        print(set_P)
        return result