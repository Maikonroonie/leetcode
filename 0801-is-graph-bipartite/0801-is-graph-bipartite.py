from collections import deque

class Solution(object):
    def isBipartite(self, graph):
        n = len(graph)
        colors = [None] * n  # None: niepokolorowany, 0 i 1 to dwa kolory
        
        for i in range(n):
            if colors[i] is None:
                colors[i] = 0  # przypisujemy pierwszy kolor
                q = deque([i])
                
                while q:
                    node = q.popleft()
                    for nb in graph[node]:
                        # Jeśli sąsiad nie ma koloru, przypisujemy mu przeciwny
                        if colors[nb] is None:
                            colors[nb] = 1 - colors[node]
                            q.append(nb)
                        # Jeśli sąsiad ma ten sam kolor, graf nie jest dwudzielny
                        elif colors[nb] == colors[node]:
                            return False
        return True
