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

'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n]

''' # druga wersja praktycznie to samo tyle ze zamina tablicy wordict na set przez co zlozonosc pesymistyczna bedzie lepsza O(n *k) n - dlugosc napisu, k - liczba slow w worddict, w pierwszym rozwiazaniu zlozonosc wychodzi O(n^2) (pesymistycznie)
