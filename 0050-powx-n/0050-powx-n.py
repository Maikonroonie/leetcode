class Solution(object):
    def myPow(self, x, n):
        def rek(x, n):
            if n==0:
                return 1
            if n <0:
                return 1/rek(x, -n)
            half = rek(x, n//2)
            if n%2==0:
                return half*half
            else:
                return half*half*x
        return rek(x, n)