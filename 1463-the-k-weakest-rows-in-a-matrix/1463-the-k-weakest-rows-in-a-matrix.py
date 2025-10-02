class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        n, m = len(mat), len(mat[0])
        # n - rows
        for row in range(n):
            row_cnt = 0
            for i in range(m):
                if mat[row][i] == 1:
                    row_cnt += 1
                else:
                    break
            heapq.heappush(heap, (row_cnt, row))
            row_cnt = 0
            
        res = []
        for i in range(k):
            cnt, r = heapq.heappop(heap)
            res.append(r)
        return res
