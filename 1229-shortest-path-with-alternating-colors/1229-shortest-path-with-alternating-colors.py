class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        graph_blue=[[] for _ in range(n)]
        graph_red=[[] for _ in range(n)]

        for v, u in redEdges:
            graph_red[v].append(u)
        for v, u in blueEdges:
            graph_blue[v].append(u)


        distance=[[float('inf'), float('inf')] for _ in range(n)]
        q=deque()
        distance[0][0]=0
        distance[0][1]=0
        q.append((0, 0))
        q.append((0, 1))
        while q:
            v, color=q.popleft()
            next_color= 1 - color
            neighbors = graph_blue[v] if color==0 else graph_red[v]
            for nb in neighbors:
                if distance[nb][next_color] == float('inf'):
                    distance[nb][next_color] = distance[v][color] +1
                    q.append((nb, next_color))


        result=[]
        for red, blue in distance:
            shortest=min(red, blue)
            result.append(shortest if shortest!=float('inf') else -1)
        return result

                    
                    
        