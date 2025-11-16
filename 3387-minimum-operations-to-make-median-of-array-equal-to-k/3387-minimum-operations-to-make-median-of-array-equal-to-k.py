from typing import List

class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        mid = n // 2   # dla parzystych: większa z dwóch środkowych — zgodnie z treścią
        res = 0

        if nums[mid] < k:
            # zwiększamy elementy od mid w prawo, które są < k
            for i in range(mid, n):
                if nums[i] < k:
                    res += k - nums[i]
                else:
                    # nie ma sensu dalej, bo po posortowaniu dalsze będą >= nums[i] >= k
                    break
        elif nums[mid] > k:
            # zmniejszamy elementy od 0 do mid, które są > k
            for i in range(mid, -1, -1):
                if nums[i] > k:
                    res += nums[i] - k
                else:
                    break

        return res
