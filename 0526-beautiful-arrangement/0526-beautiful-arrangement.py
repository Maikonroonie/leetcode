class Solution:
    def countArrangement(self, n: int) -> int:
        # zwroc liczbe ukladow ktore moge osiagnac
        # że perm[i] % i == 0 == i % perm[i] (we need one of these)

        # we want to place numbers in some positions from 0 to n-1, 
        # and bitmask will tell us which indexes are free
        # we want to place the numbers to follow two rules written on the top

        memo = {}
        def dp(i, mask):
            if i > n:
                return 1

            if mask in memo:
                return memo[mask]

            res = 0
            for j in range(1, n+1):
                if (i % j == 0 or j % i == 0) and not ((mask >> j) & 1):
                    res += dp(i+1, mask | 1 << j)
            memo[mask] = res
            return res
        return dp(1, 0)
