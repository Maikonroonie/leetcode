class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        # i guess topological sort
        graph=[[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[v].append(u)
        visited=[False for _ in range(numCourses)]
        res=[]
        def dfs(s):
            visited[s]=True
            for nb in graph[s]:
                if not visited[nb]:
                    dfs(nb)
            res.append(s)
        for i in range(numCourses):
            if not visited[i]:
                dfs(i)
        res.reverse()
        seen=[False for _ in range(numCourses)]
        for i in range(len(res)):
            seen[res[i]]=True
            for nb in graph[res[i]]:
                if seen[nb] == True:
                    return []
        return res
