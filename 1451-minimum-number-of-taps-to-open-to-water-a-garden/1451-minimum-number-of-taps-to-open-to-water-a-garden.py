class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        rg = []
        for i, r in enumerate(ranges):
            x=i-r
            y=i+r
            if i-r <= 0:
                x = 0
            if i+r >= n:
                y = n
            rg.append((x, y))

        rg.sort(key = lambda x: x[0])

        res = 0
        i=0
        cur_end = 0
        far = 0

        while cur_end < n:
            while i < len(rg) and rg[i][0] <= cur_end:
                far = max(far, rg[i][1])
                i+=1
            
            if far == cur_end: #nie da sie poszerzyc
                return -1
            
            res+=1
            cur_end = far
        return res