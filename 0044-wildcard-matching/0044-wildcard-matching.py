class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
#dp[i][j] - does s[0,..i-1] match p[0,..j-1] (True / False)
        dp[0][0] = True #emptyy string matches empty string
        #base case: matching en empty string, becouse only * can match an empty string
        for j in range(1, len(p) +1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1] 
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif p[j - 1] == "?" or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]
