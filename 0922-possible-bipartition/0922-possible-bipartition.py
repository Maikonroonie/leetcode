class Solution(object):
    def possibleBipartition(self, n, dislikes):

        graph = [[] for _ in range(n+1)]
        for v, u in dislikes:
            graph[v].append(u)
            graph[u].append(v)
        colors = [None for _ in range(n+1)]
        for i in range(n):
            if colors[i] is None:
                colors[i] = 0
                q=deque([i])
                while q:
                    node=q.pop()
                    for nb in graph[node]:
                        if colors[nb] is None:
                            colors[nb] = 1 - colors[node]
                            q.append(nb)
                        elif colors[nb] == colors[node]:
                            return False
        return True
            

        