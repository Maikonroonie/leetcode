class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:   
        #nlogn, up to n pairs, each check takes logn, but estimated is much faster
        def check(x):
            return '0' not in str(x)
        for i in range(1, n):
            j = n-i
            if check(i) and check(j):
                return [i, j]