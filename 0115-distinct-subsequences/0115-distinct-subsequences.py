class Solution(object):
    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        dp=[[0 for _ in range(n+1)] for _ in range(m+1)] #dp[m][n]
        # dp[i][j] - oznacza na ile sposobow mozna otrzymac fragmet t zaczynajacy sie na indeksie j
        # używając s zaczynajac na inseksie i
        for i in range(m+1):
            dp[i][n] = 1 

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = dp[i+1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
        return dp[0][0]