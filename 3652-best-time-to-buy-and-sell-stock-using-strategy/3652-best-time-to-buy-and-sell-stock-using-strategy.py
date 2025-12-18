from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        original = 0
        for i in range(n):
            s = strategy[i]
            p = prices[i]
            if s == -1:
                original -= p
            elif s == 1:
                original += p

        res = 0
        for i in range(k//2, n):
            if i < k:
                res += prices[i]
            else:
                s = strategy[i]
                p = prices[i]
                if s == -1:
                    res -= p
                elif s == 1:
                    res += p
        
        def f(s, p):
            if s == -1:
                return -p
            elif s == 1:
                return p
            return 0

        ans = res
        for l in range(1, n - k + 1):            
            r = l + k - 1
            ans += f(strategy[l-1], prices[l-1])

            mid_idx = l + (k // 2) - 1
            ans -= prices[mid_idx] 
            
            prev_r = strategy[r]
            
            if prev_r == 0:
                ans += prices[r]
            if prev_r == -1:
                ans += 2 * prices[r]
            elif prev_r == 1:
                pass
            res = max(res, ans)
        
        res = max(res, original)
        return res