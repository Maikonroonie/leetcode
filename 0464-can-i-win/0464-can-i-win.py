class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # maską reprezentujemy liczby ktore zostaly zużyte
        if (maxChoosableInteger * (maxChoosableInteger +1)) // 2 < desiredTotal: # suma < total
            return False
        if desiredTotal < maxChoosableInteger:
            return True # bo gracz 1 zawsze zaczyna
        
        memo = {} # maska -> bool

        def canwin(mask, remaining):
            if mask in memo:
                return memo[mask]
            for i in range(1, maxChoosableInteger +1):
                if not (mask >> i) & 1: # liczba i nie zostala uzyta & - operator i
                    if i >= remaining:
                        memo[mask] = True
                        return True
                    #jesli przeciwnik nie moze wygrac po moim ruchu
                    if not canwin(mask | (1<<i), remaining - i):
                        memo[mask] = True
                        return True
            memo[mask] = False
            return False
            
        return canwin(0, desiredTotal)

