class Solution(object):
    def allPathsSourceTarget(self, graph):
        n=len(graph)
        res=[]
        def dfs(path, node):
            if node == n-1:
                res.append(path[:])
            for nb in graph[node]:
                path.append(nb)
                dfs(path, nb)
                path.pop()
        dfs([0], 0)
        return res