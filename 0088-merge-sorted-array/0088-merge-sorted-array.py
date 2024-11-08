class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l=n+m
        while m>=1 and n>=1:
            if nums2[n-1]>nums1[m-1]:
                nums1[l-1]=nums2[n-1]
                n-=1
            else:
                nums1[l-1]=nums1[m-1]
                m-=1
            l-=1
        while n>=1:
            nums1[l-1]=nums2[n-1]
            l-=1
            n-=1



        