class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        p_ciastka=0
        p_dziecko =0
        n=len(s) # ciastka
        m=len(g) # dzieci
        res=0
        while p_ciastka < n and p_dziecko<m:
            if g[p_dziecko] <= s[p_ciastka]:
                res+=1
                p_dziecko+=1
                p_ciastka+=1

            else: p_ciastka+=1
        return res


