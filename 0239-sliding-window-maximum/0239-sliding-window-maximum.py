class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res= []
        heap = [] #maxheap
        for i, num in enumerate(nums):
            if i < k-1:
                heapq.heappush(heap, (-num, i))
            else:
                heapq.heappush(heap, (-num, i))
                val, idx = heapq.heappop(heap)
                while idx < i - k + 1:
                    val, idx = heapq.heappop(heap)
                res.append(-val)
                if idx > i - k +1:
                    heapq.heappush(heap, (val, idx))
        return res


                

        