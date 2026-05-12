class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        for u, v, w in times:
            graph[u].append((v, w))
        def dijkstra(s):
            heap = [(0, s)]
            d = [inf for _ in range(n+1)]
            d[s] = 0
            while heap:
                dist, u = heapq.heappop(heap)
                if dist > d[u]:
                    continue
                for v, w in graph[u]:
                    if d[v] > d[u] + w:
                        d[v] = d[u] + w
                        heapq.heappush(heap, (d[v], v))
            return d
        dist = dijkstra(k)
        res = max(dist[1:])
        return res if res != inf else -1 

