class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1 = set()
        s2 = set()
        s3 = set()
        s = set()
        res = []
        for num in nums1:
            s1.add(num)
        for num in nums2:
            s2.add(num)
        for num in nums3:
            s3.add(num)
        for num in nums1:
            if (num in s2 or num in s3) and num not in s:
                res.append(num)
                s.add(num)
        for num in nums2:
            if (num in s1 or num in s3) and num not in s:
                res.append(num)
                s.add(num)
        for num in nums3:
            if (num in s1 or num in s2) and num not in s:
                res.append(num)
                s.add(num)
        return res

