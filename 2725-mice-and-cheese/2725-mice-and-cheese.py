class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        heap = []
        # max-heap po (a-b): używamy ujemnego klucza
        for i in range(n):
            a, b = reward1[i], reward2[i]
            heapq.heappush(heap, (-(a - b), a, b))

        cnt = 0
        res = 0

        # Najpierw bierzemy k największych różnic -> wybieramy a
        while cnt < k:
            diff, x, y = heapq.heappop(heap)
            res += x
            cnt += 1

        # Reszta idzie do b
        while heap:
            diff, x, y = heapq.heappop(heap)
            res += y

        return res
