from math import ceil

class Solution(object):
    def minEatingSpeed(self, piles, h):
        # len(piles) >= h, wiec maksymalne h to max(piles)
        # i bs szukamy najmniejszego?

        n=len(piles)
        def is_that_k_g(k, x):
            cnt=0
            for i in range(n):
                cnt+=ceil(float(piles[i])/k)
            if cnt<= x:
                return True
            else:
                return False

        final_k = float('inf')
        min_k = 1
        max_k = max(piles)

        while min_k <= max_k:
            k = (min_k + max_k) // 2
            if is_that_k_g(k, h):
                final_k = min(final_k, k)
                max_k = k - 1
            else:
                min_k = k + 1

        return final_k

