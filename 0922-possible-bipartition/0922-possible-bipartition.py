class Solution(object):
    def possibleBipartition(self, n, dislikes):

        graph = [[] for _ in range(n+1)]
        for v, u in dislikes:
            graph[v].append(u)
            graph[u].append(v)
        colors = [None for _ in range(n+1)]
        for i in range(n):  # this is for unconneted parts of graph (unconnected graph can still be
            if colors[i] is None:                                                   #bipartitie
                colors[i] = 0 # we set two colors (0 and 1)
                q=deque([i])
                while q: # and perform deafult dfs in every connected part of the graph and check if we can
                    node=q.pop()            #color it with two colors, then we return False if we cant,
                    for nb in graph[node]:              # if we done whole graph, we return True
                        if colors[nb] is None:
                            colors[nb] = 1 - colors[node]
                            q.append(nb)
                        elif colors[nb] == colors[node]:
                            return False
        return True
            

        