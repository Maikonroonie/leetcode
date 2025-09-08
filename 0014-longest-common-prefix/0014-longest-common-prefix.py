class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        n = len(strs)
        k = inf
        for i in range(n):
            k = min(len(strs[i]), k)
        
        for i in range(k):
            st = strs[0][i]
            for j in range(1, n):
                if strs[j][i] != st:
                    return res
            res += st
        return res

