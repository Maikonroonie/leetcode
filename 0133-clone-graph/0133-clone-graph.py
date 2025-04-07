"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        visited={}
        def dfs(node):
            if node in visited:
                return visited[node]
            copy=Node(node.val)
            visited[node]=copy
            for nb in node.neighbors:
                copy.neighbors.append(dfs(nb))
            return copy
        return dfs(node) if node else None

        
