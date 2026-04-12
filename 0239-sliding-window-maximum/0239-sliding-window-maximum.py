class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
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
        '''
        # o(n) try
        res = []
        dq = deque() 
        
        for i, num in enumerate(nums):
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(i)
            
            if dq[0] < i - k + 1:
                dq.popleft()
            
            if i >= k - 1:
                res.append(nums[dq[0]])
                
        return res




                

        