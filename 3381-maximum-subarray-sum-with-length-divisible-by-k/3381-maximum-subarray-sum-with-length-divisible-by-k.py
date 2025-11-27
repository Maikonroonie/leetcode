class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # minimalna suma prefixowa dla kazdej z reszty dzielenia przez k
        min_prefix = [inf] * k
        min_prefix[0] = 0
        
        cur_sum = 0
        res = -inf
        
        for i, num in enumerate(nums):
            cur_sum += num
            
            mod_idx = (i + 1) % k
            
    # Jeśli mamy zapisaną jakąś minimalną sumę dla tej reszty, obliczamy potencjalny wynik
            if min_prefix[mod_idx] != inf:
                res = max(res, cur_sum - min_prefix[mod_idx])
            
            # Aktualizujemy minimalną sumę prefiksową dla tej reszty
            min_prefix[mod_idx] = min(min_prefix[mod_idx], cur_sum)
            
        return res if res != -inf else 0

        #brute force n^2
        '''
        # so firs we need to find biggest divisible num that is len or equal to len(nums)
        n = len(nums)
        divs = []
        if n % k == 0:
            divs.append(n)
        
        x = n
        while x >= k:
            if x % k == 0:
                divs.append(x)
            x-=1
        # teraz divs to tablica potencjalnych długosci okien
        
        # x is the len of subarray
        # now i think sliding window
        def f(x):
            l = 0
            r = x - 1
            cur_sum = sum(nums[l:r+1])
            max_sum = cur_sum

            while r < n:
                if r+1 < n:
                    cur_sum -= nums[l]
                    cur_sum += nums[r+1]
                    max_sum = max(cur_sum, max_sum)
                l+=1
                r+=1
            return max_sum
        
        res = -inf
        for div in divs:
            res = max(res, f(div))
        
        return res
        '''