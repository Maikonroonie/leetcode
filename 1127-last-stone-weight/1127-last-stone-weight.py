class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        A = []
        for stone in stones:
            heapq.heappush(A, -stone)
        #max heap 
        while len(A) > 1:
            a = heapq.heappop(A)     
            b = heapq.heappop(A)
            if a == b:
                continue
            elif a<b:
                heapq.heappush(A, (-(b-a)))
            else:
                heapq.heappush(A, (-(a-b)))
        if A:
            return -A[0]
        else:
            return 0     