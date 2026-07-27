class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        for ch in s:
            d[ch] += 1
        for ch in t:
            d[ch] -= 1
        
        for key, val in d.items():
            if val != 0:
                return False
        return True