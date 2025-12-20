class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        res = 0
        is_g = [True for _ in range(n)]
        last_letter = [None for _ in range(n)]
        
        for i in range(n):
            for idx, s in enumerate(strs):
                letter = s[i]
                if not is_g[i]:
                    continue
                elif last_letter[i] is None:
                    last_letter[i] = letter
                elif last_letter[i] <= letter:
                    last_letter[i] = letter
                else:
                    is_g[i] = False
                    res += 1
        
        return res
