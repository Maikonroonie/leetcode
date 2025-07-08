class Solution(object):
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        
        # Jeśli tablica w ogóle nie jest przekręcona, minimum jest na lewym końcu
        if nums[l] <= nums[r]:
            return nums[l]
        
        # Binary search
        while l < r:
            mid = (l + r) // 2
            
            # Jeśli środek jest większy od prawego krańca,
            # to minimum jest w prawej połowie
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                # W przeciwnym razie w lewej (łącznie ze środkiem)
                r = mid
        
        # Po wyjściu l == r -> wskazuje na najmniejszy element
        return nums[l]