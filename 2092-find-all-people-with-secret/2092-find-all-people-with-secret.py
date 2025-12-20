class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key = lambda x : x[2]) # sortujemy po czasie

        graph = [[] for _ in range(n+1)]
        for m in meetings:
            x, y, t = m
            graph[x].append((y, t))
            graph[y].append((x, t))
        
        time = [10**10 for _ in range(n)]
        time[0] = time[firstPerson] = 0
        Q = [(0, 0), (0, firstPerson)]

        while Q:
            t, u = heapq.heappop(Q)
            if t > time[u]:
                continue
            for v, mt in graph[u]:
                if mt >= t and mt < time[v]:
                    time[v] = mt
                    heapq.heappush(Q, (mt, v))
        
        return [i for i in range(n) if time[i] < 10**10]


