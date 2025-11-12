class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def gcd(a, b): # najwiekszy wspolny dzielnik
            while b:
                a, b = b, a%b
            return a

        # czyli trzeba znale pierwsze dwa takie ktorych gcd da nam 1,  a jak nie to sie nie da?
        ones = 0 
        n = len(nums)
        for num in nums:
            if num == 1:
                ones+=1
        if ones != 0:
            return n-ones
        
        res = inf

        for i in range(n):
            a = nums[i]
            for j in range(i+1, n):
                b = nums[j]
                a = gcd(a, b)
                if a == 1:
                    res = min(res, j-i)
        # teraz res to odlegolosc od dwoch elemtnow z ktorych zrobie 1
        # wiec w res ruchach utworze tą 1 i potem n-1
        return res + n-1 if res != inf else -1

