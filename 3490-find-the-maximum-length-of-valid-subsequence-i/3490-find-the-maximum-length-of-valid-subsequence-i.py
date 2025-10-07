class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        parzyste = sum(1 for x in nums if x % 2 == 0)
        nieparzyste = n - parzyste

        def f(x):
            need = x # czy robimy naprzemienne parzystych czy nieparzystych
            length = 0
            for x in nums:
                if x % 2 == need:
                    length += 1
                    need = 1 - need
            return length

        res1 = f(0)
        res2 = f(1)

        return max(parzyste, nieparzyste, res1, res2)

'''
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        # dp[i][k] = najdłuższy ważny podciąg kończący się na i,
        # gdzie wszystkie pary mają parzystość k (0 lub 1)
        dp = [[1, 1] for _ in range(n)]
        res = 1
        for i in range(n):
            for j in range(i):
                k = (nums[i] + nums[j]) % 2
                dp[i][k] = max(dp[i][k], dp[j][k] + 1)
                res = max(res, dp[i][k])
        return res
'''