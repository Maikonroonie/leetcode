class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # alice wins if sum is odd  3, 5, itd
        #jedno musi byc nieparzyste drugie parzyste 
        evenM = m//2
        oddM = m - evenM
        evenN = n//2
        oddN = n - evenN
        return (evenM * oddN) + (evenN * oddM)



'''
        #1 n payrzste m nieparz
        res = 0
        x, y = 0, 0
        for i in range(2, n+1, 2):
            x+=1
        for i in range(1, m+1, 2):
            y+=1
        res += x*y
        x, y = 0, 0
        # 2 n nieparzyste m parzyste
        for i in range(1, n+1, 2):
            x+=1
        for i in range(2, m+1, 2):
            y+=1
        res += x*y
        return res

'''
