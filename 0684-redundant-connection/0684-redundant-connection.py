
class Solution:
    def findRedundantConnection(self, edges):
        n=len(edges)
        parent=[i for i in range(n+1)]
        rank = [0 for _ in range(n+1)]
        def find(u, parent):
            if parent[u]!=u:
                parent[u]=find(parent[u], parent)
            return parent[u]
        def union(u, v, parent, rank):
            root_u = find(u, parent)
            root_v = find(v, parent)

            if root_u != root_v:
                if rank[root_u] > rank[root_v]:
                    parent[root_v] = root_u
                elif rank[root_u] < rank[root_v]:
                    parent[root_u] = root_v
                else:
                    parent[root_v] = root_u
                    rank[root_u] += 1
                return True  # Union succeeded
            return False  # u and v were already connected (cycle)
        for u, v in edges:
            if not union(u, v, parent, rank):
                return [u, v]