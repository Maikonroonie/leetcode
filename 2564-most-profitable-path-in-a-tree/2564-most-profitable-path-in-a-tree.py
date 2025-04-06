class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        # bob is going by path from node bob to node 0
        # alice is going from node 0 towards leaf (dfs) will be good here
        # we need to follow cash so alice can make money
        graph=defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited_bob=set() 
        def find_bob_path(node, target):
            if node == target:
                return [node]
            visited_bob.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited_bob:
                    path = find_bob_path(neighbor, target)
                    if path:
                        return [node] + path
            return []
            
        bob_path=find_bob_path(bob, 0)
        bob_time = [-1] * len(amount)

        for t, node in enumerate(bob_path):
            bob_time[node]=t
        
        for i in range(len(amount)):
            if bob_time[i] == -1:
                bob_time[i] = float('inf')

        cash=0
        self.max_cash=float('-inf')
        visited=set()
        def dfs_A(s, cash, time):
            visited.add(s)
            if time < bob_time[s]:
                cash+=amount[s]
            elif time == bob_time[s] and s!=0:
                cash+=amount[s]//2
            if len(graph[s])==1 and s!=0:
                self.max_cash=max(cash, self.max_cash)
            for nb in graph[s]:
                if nb not in visited:
                    dfs_A(nb, cash, time+1)
            return self.max_cash
        return dfs_A(0, 0, 0)
