class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        d = {}
        n = len(s)
        cur_len = 0
        if s[0] == "1":
            cur_len = 1
        for i in range(n-1):
            if s[i+1] == "1":
                cur_len +=1
            else:
                if cur_len not in d:
                    d[cur_len] = 1
                else:
                    d[cur_len] += 1
                cur_len = 0
        if cur_len != 0:
            if cur_len not in d:
                d[cur_len] = 1
            else:
                d[cur_len] += 1
        res = 0
        for dl, times in d.items():
            for i in range(1, dl+1):
                res += i*times
        return res % MOD

