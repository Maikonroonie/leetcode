"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]
            node_cp = Node(node.val)
            visited[node] = node_cp
            for nb in node.neighbors:
                node_cp.neighbors.append(dfs(nb))
            return node_cp
        return dfs(node) if node else None