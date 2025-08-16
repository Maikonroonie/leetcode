class Solution:
    def maximum69Number (self, num: int) -> int:
        p = -1
        n = num
        i=0
        while n > 0:
            if n % 10 == 6:
                p = i
            n//=10
            i+=1
        if p != -1: # jesli znalezlismy jakas 6
            num += 3 * (10**p)
        return num 
        