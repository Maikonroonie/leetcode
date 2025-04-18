class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        graph=[[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        graph_copy=[[] for _ in range(n)]
        for u, v in edges:
            graph_copy[u].append(v)
            graph_copy[v].append(u)
        
        ans=0
        def dfs(node, prev, depth):
            total=1
            nonlocal ans
            ans+=depth
            for child in graph[node]:
                if child == prev:
                    continue
                total+=dfs(child, node, depth+1)
            graph_copy[node]=total
            return total
        dfs(0, None, 0)
        res=[0 for _ in range(n)]
        res[0] = ans
        def dfs2(node, prev):
            for child in graph[node]:
                if child == prev:
                    continue
                res[child] = res[node] - graph_copy[child] + (n-graph_copy[child])
                dfs2(child, node)
        dfs2(0,None)
        return res