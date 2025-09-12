class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {"a", "e", "i", "o", "u"}
        n = len(s)
        idx_of_vowels = set()
        num_of_vowels = 0
        for i, chr in enumerate(s):
            if chr in vowels:
                idx_of_vowels.add(i)
                num_of_vowels += 1
        if num_of_vowels == 0:
            return False
        if num_of_vowels % 2 == 1:
            return True
        if num_of_vowels % 2 == 0:
            return True

