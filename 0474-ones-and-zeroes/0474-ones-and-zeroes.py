class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def count(s):
            c0, c1 = 0, 0
            for chr in s:
                if chr == "0":
                    c0 += 1
                elif chr == "1":
                    c1 += 1
            return c0, c1

        

        # dp[i][j] = maks liczba stringów używając i zer i j jedynek
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            c0, c1 = count(s)
            # iterujemy "wstecz" żeby każdy string użyć tylko raz
            for i in range(m, c0 - 1, -1):
                for j in range(n, c1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - c0][j - c1] + 1)

        return dp[m][n]
        
    


                


        