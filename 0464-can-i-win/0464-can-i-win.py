#top - bottom
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
'''
#bottom - up
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False
        if desiredTotal <= maxChoosableInteger:
            return True

        n = maxChoosableInteger
        total_states = 1 << n #ilosc wzsystkich masek chyba to bedzie 2^n
        DP = [False] * total_states
        sums = [0] * total_states   # sums[mask] = suma wybranych liczb w masce

        # precompute sums
        for mask in range(total_states):
            s = 0
            for i in range(n):
                if (mask >> i) & 1:
                    s += i+1
            sums[mask] = s

        # przechodzimy po wszystkich stanach od pełnych masek do pustej
        for mask in range(total_states-1, -1, -1):
            for i in range(n):
                if not (mask >> i) & 1:  # liczba (i+1) jest wolna, czyli na pozyci i od prawej
                    if sums[mask] + (i+1) >= desiredTotal:
                        DP[mask] = True
                        break
                    if not DP[mask | (1<<i)]: #stan po tym jak wybiore i+1
                        DP[mask] = True # czyli jesli w kolejnym stanie nie da sie wygrac
                        break # to w tym wygralismy i essa (wybierajac liczbe i+1)

        return DP[0] # zwracamy dp[0] - bo to stan poczatkowy zadna liczba nie zostala uzyta

'''
