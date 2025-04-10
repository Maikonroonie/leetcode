class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph=[[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[u].append(v)
        # graf nie moze miec cyklow chyba if cykl return false else return true
        visited = [0] * numCourses
        def dfs(s):
            if visited[s]==1:
                return False
            if visited[s]==2:
                return True
            visited[s]=1
            for nb in graph[s]:
                if dfs(nb) == False:
                    return False
            visited[s]=2
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True
