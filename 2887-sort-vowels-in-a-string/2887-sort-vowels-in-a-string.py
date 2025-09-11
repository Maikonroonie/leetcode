class Solution:
    def sortVowels(self, s: str) -> str:
        map = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
        st1 = ""
        st2 = ""
        idx = set()
        for i, chr in enumerate(s):
            if chr in map:
                st1 += chr
                idx.add(i)
            else:
                st2 += chr
        st1 = sorted(st1)
        res = ""
        p1 = 0
        p2 = 0
        for i in range(len(s)):
            if i in idx:
                res += st1[p1]
                p1 += 1
            else:
                res += st2[p2]
                p2 += 1
        return res
         