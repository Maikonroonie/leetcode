#nlogn, not quite optimal
'''
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        n = len(nums)
        mid = (n - 1) // 2  # środkowa część dla dolnej połowy
        left = nums[:mid+1]  # mniejsze
        right = nums[mid+1:] # większe

        # Wstawiamy od końca, aby uniknąć problemu z powtarzającymi się liczbami
        l_idx = mid
        r_idx = len(right) - 1
        for i in range(n):
            if i % 2 == 0:
                nums[i] = left[l_idx]
                l_idx -= 1
            else:
                nums[i] = right[r_idx]
                r_idx -= 1
'''

# o(n) with the quick select algorithm
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        if n <= 1:
            return

        # Quickselect
        def partition(T, l, r):
            x = T[r]
            i = l - 1
            for j in range(l, r):
                if T[j] <= x:
                    i += 1
                    T[j], T[i] = T[i], T[j]
            T[i+1], T[r] = T[r], T[i+1]
            return i+1

        def quick_select(T, l, r, k):
            if l == r:
                return T[l]
            p = partition(T, l, r)
            if p == k:
                return T[p]
            elif p < k:
                return quick_select(T, p+1, r, k)
            else:
                return quick_select(T, l, p-1, k)

        median = quick_select(nums[:], 0, n-1, (n-1)//2)

# -------------------
        # Virtual index mapping
        # -------------------
        def A(i):
            return (1 + 2*i) % (n | 1)

        # -------------------
        # 3-way partitioning (Dutch National Flag)
        # -------------------
        left, i, right = 0, 0, n - 1
        while i <= right:
            if nums[A(i)] > median:
                nums[A(left)], nums[A(i)] = nums[A(i)], nums[A(left)]
                left += 1
                i += 1
            elif nums[A(i)] < median:
                nums[A(right)], nums[A(i)] = nums[A(i)], nums[A(right)]
                right -= 1
            else:
                i += 1