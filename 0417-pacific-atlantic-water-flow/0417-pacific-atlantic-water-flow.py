class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        res = []
        stack = []
        # first we try to get from pacific to atalantic 
        P_set = set()
        #visited = set()
        for i in range(n):
            stack.append((i, 0))
            P_set.add((i, 0))
           # visited.add((i, 0))
        for j in range(m):
            stack.append((0, j))
            P_set.add((0, j))
           # visited.add((0, j))
        while stack:
            r, c = stack.pop()
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr, nc = r + dx, c + dy
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in P_set:
                    if heights[nr][nc] >= heights[r][c]:
                        stack.append((nr, nc))
                        #visited.add((nr, nc))
                        P_set.add((nr, nc))
        
        # we do same thing for atlantic ocean
        A_set = set()
        for i in range(n):
            stack.append((i, m-1))
            A_set.add((i, m-1))
        for j in range(m):
            stack.append((n-1, j))
            A_set.add((n-1, j))
        while stack:
            r, c = stack.pop()
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr, nc = r + dx, c + dy
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in A_set:
                    if heights[nr][nc] >= heights[r][c]:
                        stack.append((nr, nc))
                        A_set.add((nr, nc))
        
        for i in range(n):
            for j in range(m):
                if (i, j) in P_set and (i, j) in A_set:
                    res.append((i, j))
        return res
