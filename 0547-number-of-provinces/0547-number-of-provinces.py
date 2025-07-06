class Solution(object):
    def findCircleNum(self, isConnected):
        n=len(isConnected)
        graph=[[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and i>j:
                    graph[i].append(j)
                    graph[j].append(i)
        cnt=0

        visited=[False for _ in range(n)]

        def dfs(s):
            visited[s] = True

            for u in graph[s]:
                if not visited[u]:
                    dfs(u)
        for i in range(n):
            if visited[i] == False:
                cnt+=1
                dfs(i)
        return cnt
                    
        