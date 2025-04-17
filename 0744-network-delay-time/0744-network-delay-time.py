class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph=[[] for _ in range(n+1)]
        for u, v, w in times:
            graph[u].append((v, w))
        
        #DIJKSTRA algorithm :)
        d=[float('inf') for _ in range(n+1)]
        d[k]=0
        Q=[]
        heapq.heappush(Q, (d[k], k))
        while Q:
            dist, u = heapq.heappop(Q)
            if dist > d[u]:
                continue
            for nb, weight in graph[u]:
                if d[nb] > d[u] + weight:
                    d[nb] = d[u] + weight
                    heapq.heappush(Q, (d[nb], nb))
        res = max(d[1:])
        return res if res!=float('inf') else -1