class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        x=0
        T=[0 for i in range(m+n)]
        for i in range(m):
            T[i]=nums1[i]
        for i in range(m,m+n):
            T[i]=nums2[x]
            x+=1
        T.sort()
        if (n+m)%2==0:
            return (T[(n+m)//2]+T[(n+m-2)//2])/2
        else:
            return T[(n+m-1)//2]
        