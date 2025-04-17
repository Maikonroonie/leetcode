class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n ==1:
            return [0]
        graph=[[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        leaves=deque()
        edge_cnt=[0 for _ in range(n)]
        for i in range(n):
            if len(graph[i])==1:
                leaves.append(i)
            edge_cnt[i]=len(graph[i])
        while leaves:
            if n<=2:
                return(list(leaves))
            for i in range(len(leaves)):
                node=leaves.popleft()
                n-=1
                for nb in graph[node]:
                    edge_cnt[nb]-=1
                    if edge_cnt[nb]==1:
                        leaves.append(nb)
        
                