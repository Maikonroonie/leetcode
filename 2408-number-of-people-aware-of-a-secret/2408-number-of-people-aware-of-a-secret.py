class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0 for _ in range(n+1)] #dp[i] num of people who lernt secret on day i
        dp[1] = 1
        with_secret = 0
        mod = 10**9 + 7
        for i in range(2, n+1):
            
            remember = dp[i-delay] if i-delay >=1 else 0

            forgoten = dp[i-forget] if i-forget >=1 else 0

            with_secret = (with_secret + remember - forgoten + mod)%mod
            dp[i] = with_secret
        res = 0
        for i in range(n-forget+1, n+1):
            if i>=1:
                res = (res + dp[i]) % mod

        return res
