class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        n = max(max(u, v) for u, v in edges)
        graph = [[] for _ in range(n+1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # now we need to find shortest cycle in that graph
        # i think just bfs
        # bfs from every v?

        def bfs(G, i, visited, dist):
            q = deque()
            dist[i] = 0
            q.append((i, -1))
            res = inf

            while q:
                u, parent = q.popleft()
                visited[u] = True

                for v in G[u]:
                    if not visited[v]:
                        dist[v] = dist[u] + 1
                        q.append((v, u))
                    elif v != parent: # v was already visited
                        lenght = dist[u] + dist[v] + 1
                        res = min(res, lenght)
            return res

# ogolnie to jest troche brzydko napisane, bo ladniej by bylo jakby dist było 
# napisane w funkcji bfs, a visited moze by nie bylo potrzebne bo by wystraczylo
# sprawdzac czy dist[u] == -1, bo jak jest to znaczy ze u jest not visited
        ans = inf
        for u in range(n):
            dist = [-1 for _ in range(n+1)]
            visited = [False for _ in range(n+1)]
            ans = min(ans, bfs(graph, u, visited, dist))
        return ans if ans != inf else -1




            

