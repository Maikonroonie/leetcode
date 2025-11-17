class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        res = 0
        n = len(complexity)
        # pierwszy musi być najmniejszy a reszta to po prostu silnia n-1
        def silnia(a):
            res = 1
            for i in range(2, a+1):
                res *= i
            return res
        
        d = {}
        for num in complexity:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        small = inf
        how_many = 0
        for num, times in d.items():
            if num < small:
                small = num
                how_many = times

        
        if how_many == 1 and small == complexity[0]:
            return silnia(n-1) % MOD
        else:
            return 0



