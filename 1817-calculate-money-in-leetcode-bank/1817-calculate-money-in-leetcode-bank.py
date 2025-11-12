class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        md = 0

        for i in range(n):
            if i%7 == 0: #mamy poniedzialek
                md += 1
                res += md
                week = md
            else:
                week += 1
                res += week
        return res
            