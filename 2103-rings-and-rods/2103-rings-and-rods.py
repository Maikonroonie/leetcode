class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)
        s = [set() for _ in range(10)]
        for i in range(0, n, 2):
            color = rings[i]
            pos = int(rings[i+1])
            s[pos].add(color)
        res = 0
        for i in range(10):
            st = s[i]
            if 'R' in st and 'G' in st and 'B' in st:
                res += 1
        return res


        