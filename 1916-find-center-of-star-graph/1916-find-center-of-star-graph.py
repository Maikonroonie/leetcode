class Solution(object):
    def findCenter(self, edges):
        graph=collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        n=len(edges)
        for i in range(1, n+2):
            if len(graph[i])==(n):
                return i
        
