class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for a in range(1, n):
            for b in range(1, n):
                c = sqrt(a**2 + b**2)
                if c > n:
                    break
                elif c == round(c):
                    res+=1 
        return res