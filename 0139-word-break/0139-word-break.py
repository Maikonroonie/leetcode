class Solution(object):
    def wordBreak(self, s, wordDict):
        n=len(s)
        dp=[False for _ in range(n+1)]
        dp[0] = True
        for i in range(n+1):
            for word in wordDict:
                if len(word) <= i and word == s[i-len(word):i] and dp[i-len(word)] == True:
                    dp[i] = True
        return dp[n]
