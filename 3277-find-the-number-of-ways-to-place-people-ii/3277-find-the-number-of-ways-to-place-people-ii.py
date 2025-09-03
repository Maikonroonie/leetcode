class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n=len(points)
        points.sort(key = lambda x: (x[0], -x[1]))
        res = 0

        for i , (x, y) in enumerate(points):
            maxY = -inf
            for j in range(i+1, n):
                x2, y2 = points[j]
                if y >= y2 > maxY:
                    res+=1
                    maxY = y2
        return res

