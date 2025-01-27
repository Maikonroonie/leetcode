class Solution(object):
    def fib(self, n):
        def rek(n):
            if n==0:
                return 0
            if n==1 or n==2:
                return 1
            return rek(n-1) + rek(n-2)
        return rek(n)