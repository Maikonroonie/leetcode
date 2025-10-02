class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = [ None for _ in range(len(score))]
        heap = []
        for i, scr in enumerate(score):
            heapq.heappush(heap, (-scr, i)) # - so max heap
        
        cur = 1
        while heap:
            scr, i = heapq.heappop(heap) # najlepszy
            if cur == 1:
                res[i] = 'Gold Medal'
                cur+=1
            elif cur == 2:
                res[i] = 'Silver Medal'
                cur+=1
            elif cur == 3:
                res[i] = 'Bronze Medal'
                cur+=1
            else:
                res[i] = str(cur)
                cur+=1
        return res

        
        