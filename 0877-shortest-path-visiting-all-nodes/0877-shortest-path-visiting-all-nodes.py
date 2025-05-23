class Solution(object):
    def shortestPathLength(self, graph):
        n = len(graph)
        queue = deque()
        visited = [[False] * (1 << n) for _ in range(n)]
        
        for i in range(n):
            queue.append((i, 1 << i, 0))  # (node, visited_mask, path_length)
            visited[i][1 << i] = True
        
        while queue:
            node, mask, dist = queue.popleft()
            if mask == (1 << n) - 1:
                return dist
            for neighbor in graph[node]:
                next_mask = mask | (1 << neighbor)
                if not visited[neighbor][next_mask]:
                    visited[neighbor][next_mask] = True
                    queue.append((neighbor, next_mask, dist + 1))


# we have to find shortest path visiting all nodes in whole undirected graph, that means we can start
#wherever. 

#the first time we reach mask = (1<<n) - 1 (for example for n=5, 10000-1 = 01111) we reached the end 
#for the first time so the distance is the shortest becouse we do bfs, so we return it