class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # i ll try merge sort
        def merge(A, B):
            C = []
            ap = 0
            bp = 0
            while ap < len(A) and bp < len(B):
                if A[ap] < B[bp]:
                    C.append(A[ap])
                    ap += 1
                else:
                    C.append(B[bp])
                    bp += 1
            while ap < len(A):
                C.append(A[ap])
                ap += 1
            while bp < len(B):
                C.append(B[bp])
                bp += 1
            return C
        def merge_sort(A):
            n = len(A)
            if n >= 2:
                mid = n//2
                left = A[:mid]
                right = A[mid:]
                return merge(merge_sort(left), merge_sort(right))
            else:
                return A

        return merge_sort(nums)