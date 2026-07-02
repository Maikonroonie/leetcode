class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = defaultdict(int)
        for ch in s:
            d[ch] += 1
        for c in t:
            if c not in d:
                return c
            if c in d:
                d[c] -=1
            if d[c] < 0:
                return c