class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        m = max(len(nums[i]) for i in range(n))


        # diag to bedzie x + y
        diags = [[] for _ in range(m+n-1) ]
        for i in range(n):
            for j in range(len(nums[i])):
                diags[j + i].append(nums[i][j])
        
        res = []
        for diag in diags:
            for i in range(len(diag)-1, -1, -1):
                res.append(diag[i])
        return res

