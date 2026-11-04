class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vows_set = {"a", "e", "i", "o", "u"}
        
        i = len(s) - 1
        while i >= 0 and s[i] in vows_set:
            i -= 1
            
        return s[:i + 1]