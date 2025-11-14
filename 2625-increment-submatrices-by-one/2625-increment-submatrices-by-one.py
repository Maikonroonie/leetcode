class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        # brute
        '''
        def add(x1, y1, x2, y2):
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    matrix[y][x] += 1
        for x in queries:
            y1, x1, y2, x2 = x
            add(x1, y1, x2, y2)
        return matrix
        '''
        diff = [[0 for _ in range(n)] for _ in range(n)]
        for y1, x1, y2, x2 in queries:
            for i in range(y1, y2 + 1):
                diff[i][x1] += 1
                if x2 + 1 < n:
                    diff[i][x2 + 1] -= 1
        
        for i in range(n):
            for j in range(1, n):
                diff[i][j] += diff[i][j - 1]

        return diff