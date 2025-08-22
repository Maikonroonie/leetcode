class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)

        prefix_max = [0 for _ in range(n)]            
        suffix_min = [0 for _ in range(n)]       

        prefix_max[0] = arr[0]

        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], arr[i])
        
        suffix_min[-1] = arr[-1]

        for i in range(n-2, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], arr[i])
        
        res = 1
        for i in range(n-1):
            if prefix_max[i] <= suffix_min[i+1]:
                res+=1
        
        return res


