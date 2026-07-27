class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
        heap = []
        cur = 0
        for num, times in cnt.items():
            if cur < k:
                heapq.heappush(heap, (times, num))
                cur += 1
            else:
                tup = heapq.heappop(heap)
                if tup[0] > times:
                    heapq.heappush(heap, tup)
                else:
                    heapq.heappush(heap, (times, num))        
        res = []
        for t, n in heap:
            res.append(n)
        return res

