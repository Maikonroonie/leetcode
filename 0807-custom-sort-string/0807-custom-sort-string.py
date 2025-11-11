class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # so chrs in string order are the ones we have to keep in order in the output

        d = defaultdict()
        res = ""
        for i, chr in enumerate(s):
            if chr not in d:
                d[chr] = 1
            else:
                d[chr] += 1

        for chr in order:
            if chr in d and d[chr] != 0:
                for _ in range(d[chr]):
                    res += chr
                    d[chr] -= 1
            
        for key, val in d.items():
            if val > 0:
                for _ in range(val):
                    res += key

        return res



        


