class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        right_count = Counter(nums)
        left_count = Counter()
        
        res = 0
        
        for num in nums:
            #num jest teraz środkiem, usuwamy go z prawej strony
            right_count[num] -= 1
            
            target = num * 2
            
            # Sprawdzamy, czy mamy pasujące 2num po lewej i po prawej
            if left_count[target] > 0 and right_count[target] > 0:
                # Ilość kombinacji to iloczyn wystąpień po lewej i prawej
                count = left_count[target] * right_count[target]
                res = (res + count) % MOD
            
            # 4. Na koniec obecnej iteracji, 'num' staje się częścią "lewej strony" dla
            # kolejnych elementów
            left_count[num] += 1
            
        return res
            
        