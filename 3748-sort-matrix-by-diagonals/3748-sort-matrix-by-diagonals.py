class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        # there is 2n - 1 diags
        diags = defaultdict(list)
        for y in range(n):
            for x in range(n):
                diags[x-y].append(grid[y][x])
        

        for key, lists in diags.items():
            if key>0:
                lists.sort()
            else:
                lists.sort(reverse = True)
                
        A = [[0 for _ in range(n)] for _ in range(n)]
        for y in range(n):
            for x in range(n):
                A[y][x] = diags[x-y].pop(0)

        return A




        return []
