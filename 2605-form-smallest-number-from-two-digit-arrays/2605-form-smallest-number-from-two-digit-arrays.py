class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        d = set()
        if n <= m:
            nums1.sort()
            for num in nums2:
                d.add(num)
            for nm in nums1:
                if nm in d:
                    return nm
        else:
            nums2.sort()
            for num in nums1:
                d.add(num)
            for nm in nums2:
                if nm in d:
                    return nm
        d1 = nums1[0]
        d2 = nums2[0]
        if d1 == d2:
            return d1
        if d1 < d2:
            res = d1*10 + d2
        else:
            res = d2*10 + d1

        def sol(A, s, ans):
            for i in range(1, len(A)):
                num = s*10 + A[i]
                if num < ans:
                    ans = num
                num = A[i] *10 + s
                if num < ans:
                    ans = num
            return ans
        if n <= m:
            return sol(nums2, d1, res)
        else:
            return sol(nums1, d2, res)
        
