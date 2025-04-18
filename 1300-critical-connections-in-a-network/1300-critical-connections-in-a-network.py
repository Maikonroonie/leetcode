class Solution(object):
    def criticalConnections(self, n, connections):
        graph=[[] for _ in range(n)]
        for v, u in connections:
            graph[v].append(u)
            graph[u].append(v)

        #find bridges in undirected graph
        bridges=[]
        time=0
        visited=[False for _ in range(n)]
        low = [float('inf') for _ in range(n)]
        discovery = [0 for _ in range(n)]
        def dfs_visit(v, parent=-1):
            nonlocal time, discovery, visited
            time+=1
            low[v]=discovery[v]=time

            for u in graph[v]:
                if not visited[u]:
                    visited[u]=True
                    dfs_visit(u, v)

                    low[v]=min(low[v], low[u])

                    if low[u] > discovery[v]:
                        bridges.append((v, u))
                elif u != parent:
                    low[v]=min(low[v], discovery[u])

        for v in range(n):
            if not visited[v]:
                visited[v]=True
                dfs_visit(v)
        return bridges
    