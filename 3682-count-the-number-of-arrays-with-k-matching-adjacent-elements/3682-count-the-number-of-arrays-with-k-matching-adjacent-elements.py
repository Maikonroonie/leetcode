class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # n is the len of arr
        # m is the range of how big can each num be in arr
        # k is the number of matching adjacent emelents in arr
        MOD = 10**9 + 7

        if k < 0 or k > n-1:
            return 0

        # precomputujemy silnie do n-1
        fact = [1] * (n)
        for i in range(1, n):
            fact[i] = fact[i-1] * i % MOD

        def modinv(x):
            return pow(x, MOD-2, MOD)

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * modinv(fact[b] * fact[a-b] % MOD) % MOD

        c = comb(n-1, k)
        power = pow(m-1, n-k-1, MOD) if n-k-1 >= 0 else 1
        ans = c * m % MOD * power % MOD
        return ans
