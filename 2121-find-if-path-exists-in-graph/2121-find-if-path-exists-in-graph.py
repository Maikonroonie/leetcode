class Solution(object):
    def validPath(self, n, edges, source, destination):
        if n==1 and not edges:
            return True
        def edges_list_to_graph(edges):
            graph = {}
            for u, v in edges:
                if u not in graph:
                    graph[u] = []
                if v not in graph:
                    graph[v] = []
                graph[u].append(v)
                graph[v].append(u)
            return graph

        def dfs(graph, start, visited=None):
            if visited is None:
                visited = set()
            visited.add(start)
            for neighbor in graph[start]:
                if neighbor == destination:
                    return True
                if neighbor not in visited:
                    if dfs(graph, neighbor, visited):
                        return True
            return False

        graph = edges_list_to_graph(edges)
        return dfs(graph, source)
