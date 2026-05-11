from collections import deque
# topological sort (khan)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        count = 0
        while q:
            node = q.popleft()
            count += 1
            
            for next_node in adj[node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    q.append(next_node)

        return count == numCourses