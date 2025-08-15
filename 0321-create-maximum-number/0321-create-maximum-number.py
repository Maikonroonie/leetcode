from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # wybiera leksykograficznie największy podciąg długości t z nums
        def pick(nums, t):
            drop = len(nums) - t
            stack = []
            for x in nums:
                while drop and stack and stack[-1] < x:
                    stack.pop()
                    drop -= 1
                stack.append(x)
            return stack[:t]

        # porównuje a[i:] i b[j:] leksykograficznie
        def greater(a, i, b, j):
            while i < len(a) and j < len(b) and a[i] == b[j]:
                i += 1
                j += 1
            if j == len(b):
                return True
            if i == len(a):
                return False
            return a[i] > b[j]

        # scala dwa podciągi w największą możliwą liczbę
        def merge(a, b):
            i = j = 0
            out = []
            while i < len(a) or j < len(b):
                if greater(a, i, b, j):
                    out.append(a[i]); i += 1
                else:
                    out.append(b[j]); j += 1
            return out

        m, n = len(nums1), len(nums2)
        start = max(0, k - n)
        end = min(k, m)
        best = []
        found = False

        for i in range(start, end + 1):
            a = pick(nums1, i)
            b = pick(nums2, k - i)
            cand = merge(a, b)
            if not found or greater(cand, 0, best, 0):
                best = cand
                found = True

        return best
