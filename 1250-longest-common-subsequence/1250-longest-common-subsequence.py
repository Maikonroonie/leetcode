class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        memo = {}
        
        def lcs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + lcs(i + 1, j + 1)
            else:
                memo[(i, j)] = max(lcs(i + 1, j), lcs(i, j + 1))
            
            return memo[(i, j)]
        
        return lcs(0, 0)



    '''
    class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        n = len(text1)
        m = len(text2)
        
        # Tworzymy tablicę (n+1) x (m+1)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[n][m]
'''