class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        d = {} # illsc ciagow zer o danej długosci

        l = 0
        dlg = 0
        for num in nums:
            if num == 0:
                dlg += 1
            elif dlg > 0:
                if dlg not in d:
                    d[dlg] = 1
                else:
                    d[dlg] += 1
                dlg = 0
        if dlg > 0:
            if dlg not in d:
                d[dlg] = 1
            else:
                d[dlg] += 1

        res = 0 
        for size, times in d.items():
            for i in range(1, size+1):
                res += i * times
        return res