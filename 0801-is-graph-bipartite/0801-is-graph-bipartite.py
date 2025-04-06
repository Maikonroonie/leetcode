'''class Solution(object):
    def isBipartite(self, graph):
        set_a=set()
        set_b=set()

        def bfs(graph, s, start_set, sec_set):
            visited=set()
            q=deque([s])
            visited.add(s)
            start_set.add(s)
            while q:
                node=q.popleft()
                for nb in graph[node]:
                    if node in start_set:
                        sec_set.add(nb)
                    else:
                        start_set.add(nb)
                    if nb not in visited:
                        visited.add(nb)
                        q.append(nb)
            x=0
            while x<len(graph):
                if x not in visited:
                    if len(set_a)<=len(set_b):
                        bfs(graph, x, set_a, set_b)
                    else:
                        bfs(graph, x, set_b, set_a)
                x+=1
            if len(set_a)==len(set_b)==len(graph)//2 and len(graph)%2==0:
                return True
            elif len(graph)%2==1 and len(set_a)==(len(set_b)+1):
                return True
            else:
                return False
        return bfs(graph, 0, set_a, set_b)
        '''
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



