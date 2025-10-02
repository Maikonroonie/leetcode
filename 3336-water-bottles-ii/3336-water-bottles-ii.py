class Solution:
    def maxBottlesDrunk(self, numBottles: int, n: int) -> int:
        res = 0
        cur = numBottles
        while cur >= n:
            res+=n
            cur = cur - n + 1
            n+=1
        
        return res + cur