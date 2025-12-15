class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        A = []
        l = 1
        prev = prices[0]
        for i in range(1, n):
            num = prices[i]
            if num == prev - 1:
                l += 1
                prev = num
            else:
                A.append(l)
                l = 1
                prev = num
        A.append(l)
        #print(A)
        def calculate(a):
            res = 0
            for i in range(a):
                res += i+1
            return res
        res = 0
        for num in A:
            res += calculate(num)
        return res

        