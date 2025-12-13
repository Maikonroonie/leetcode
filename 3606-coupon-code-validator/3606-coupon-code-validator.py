class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        g = {"electronics":0, "grocery":1, "pharmacy":2, "restaurant":3}
        res = []
        n = len(code)
        def is_g(s):
            return len(s) > 0 and all(c.isalnum() or c == '_' for c in s)

        for i in range(n):
            if isActive[i] and businessLine[i] in g and is_g(code[i]):
                res.append((g[businessLine[i]], code[i]))
        res.sort()

        return [x for _, x in res]