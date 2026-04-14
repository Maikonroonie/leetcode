class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        pn = 0
        pm = 0
        res = ''
        while pn < n and pm < m:
            if pn == pm:
                res += (word1[pn])
                pn += 1
            else:
                res += (word2[pm])
                pm += 1
        while pn < n:
            res += (word1[pn])
            pn += 1
        while pm < m:
            res += (word2[pm])
            pm += 1
        return res




        