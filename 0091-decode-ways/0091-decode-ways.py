class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        
        dp = [0] * (n + 1)
        dp[0] = 1  # pusty string: 1 sposób
        dp[1] = 1  # pierwszy znak (jeśli nie '0') ma 1 sposób
        
        for i in range(2, n + 1):
            # Pojedynczy znak
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            # Para znaków
            if '10' <= s[i - 2:i] <= '26':
                dp[i] += dp[i - 2]
        
        return dp[n]